from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
from repository.VerificationRepository import VerificationRepository
from Domain.models.QuestionsDomainModel import QuestionsDomainModel
import re
import random
from flask import Flask, request
import base64
from config.config import api_secret
import jwt
import hashlib


class ResetPasswordService:
    repository: VerificationRepository
    auth: AuthorizationManager

    regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    def __init__(self, repository: VerificationRepository,  auth: AuthorizationManager):
        self.repository = repository
        self.auth = auth

    def show_question(self, email: str):

        if re.search(self.regex, email):
            record = self.repository.find_record_by_email(email)
            if record is not None:
                print(record)

                model = QuestionsDomainModel('question_one', 'question_two', 'question_three', '1', '2', '3')
                questions = model.to_list()
                question = random.sample(questions, 2)

                user_id = str(record['_id'])
                token = self.auth.make_token_for_user_id(user_id)
                data = {
                    "questions": question,
                    "resetToken": token
                }
                return data

            raise Exception("The email you entered doesn't belong to an account.Please check your email and try again.")

        raise ValueError

    def change_password(self, json):
        if request.headers.get('authorization') is None:
            return {'success': False}, 401
        else:
            encode_token = request.headers['authorization']

        decoded_token = jwt.decode(encode_token, api_secret, algorithms="HS256")
        _id = decoded_token['id']
        print(_id)

        record = self.repository.find_record_by_user_id(_id)
        if record is not None:

            ans_one = json[0]
            ans_two = json[1]
            password = json[2]
            print(password)
            hashed_password = hashlib.md5(password['new_password'].encode('utf-8')).hexdigest()

            if ans_one['question_id'] == '1' and ans_two['question_id'] == '2':
                if ans_one['answer'] == record['answer_one'] and ans_two['answer'] == record['answer_two']:
                    self.repository.update_password(record, hashed_password)
                    print(self.repository.find_record_by_user_id(_id))
                    return True

                raise Exception("the answer you entered is wrong")

            if ans_one['question_id'] == '1' and ans_two['question_id'] == '3':
                if ans_one['answer'] == record['answer_one'] and ans_two['answer'] == record['answer_three']:
                    self.repository.update_password(record, hashed_password)
                    return True

                raise Exception("the answer you entered is wrong")

            if ans_one['question_id'] == '2' and ans_two['question_id'] == '3':
                if ans_one['answer'] == record['answer_two'] and ans_two['answer'] == record['answer_three']:
                    self.repository.update_password(record, hashed_password)
                    return True

                raise Exception("the answer you entered is wrong")

            raise Exception("the user_id you entered doesn't exist")

        raise Exception("The id you entered doesn't belong to an account.Please check your token and try again.")









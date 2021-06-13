from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
from repository.VerificationRepository import VerificationRepository
from Domain.models.RegisterUserDomainModel import RegisterUserDomainModel
import re
import datetime
import hashlib


class RegisterService:
    repository: VerificationRepository
    auth: AuthorizationManager

    regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    def __init__(self, repository: VerificationRepository,  auth: AuthorizationManager):
        self.repository = repository
        self.auth = auth

    def register_user(self, json: str) -> str:

        if re.search(self.regex, json['email']):
            record = self.repository.find_record_by_email(json['email'])

            if record is None:
                if json['password'] == json['confirm_password']:

                    hashed_password = hashlib.md5(json['password'].encode('utf-8')).hexdigest()
                    time = datetime.datetime.now()
                    model = RegisterUserDomainModel(json['email'], hashed_password, time,
                                                       json['answer_one'],
                                                       json['answer_two'],
                                                       json['answer_three'])
                    inserted_id = self.repository.insert(model)
                    print(inserted_id)
                    token = self.auth.make_token_for_user_id(inserted_id)
                    return token

                raise Exception("Sorry, password & confirm-pass is not equal")

            raise Exception("This email isn't available. Please try another.")

        raise ValueError













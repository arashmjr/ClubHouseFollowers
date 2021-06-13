from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
from repository.VerificationRepository import VerificationRepository
from Domain.models.RegisterUserDomainModel import RegisterUserDomainModel
import re
import hashlib, uuid


class LoginService:
    repository: VerificationRepository
    auth: AuthorizationManager

    regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    def __init__(self, repository: VerificationRepository,  auth: AuthorizationManager):
        self.repository = repository
        self.auth = auth

    def login_user(self, json: str) -> str:

        if re.search(self.regex, json['email']):
            record = self.repository.find_record_by_email(json['email'])
            if record is not None:
                hashed_password = hashlib.md5(json['password'].encode('utf-8')).hexdigest()
                if record['password'] == hashed_password:
                    user_id = str(record['_id'])
                    token = self.auth.make_token_for_user_id(user_id)
                    return token

                raise Exception("Sorry, your password was incorrect. Please double-check your password.")

            raise Exception("The email you entered doesn't belong to an account.Please check your email and try again.")

        raise ValueError







from flask import Request
from config.config import api_secret
from datetime import datetime, timedelta
import jwt
from functools import wraps
from flask import Flask, abort, request


class AuthorizationManager:
    # __instance = None
    #
    # def __init__(self):
    #     if AuthorizationManager.__instance is not None:
    #         raise Exception("This class is a singleton!")
    #     else:
    #         AuthorizationManager.__instance = self
    #
    # @staticmethod
    # def get_instance():
    #     if AuthorizationManager.__instance is None:
    #         AuthorizationManager()
    #     return AuthorizationManager.__instance

    def make_token_for_user_id(self, user_id: str) -> str:
        token = jwt.encode({'id': user_id, 'exp': datetime.utcnow() + timedelta(days=7)}, api_secret, algorithm='HS256')
        return token

    def is_valid_request(self, request: Request):
        if "Authorization" in request.headers:
            try:
                encoded_jwt = request.headers["Authorization"]
                res = jwt.decode(encoded_jwt, api_secret, algorithms=['HS256'])
                if "id" in res:
                    return True
                return False
            except Exception as e:
                return False
        return False

    def extract_user_id(self, request: Request):
        if self.is_valid_request(request):
            encoded_jwt = request.headers.get("Authorization")
            res = jwt.decode(encoded_jwt, api_secret, algorithms=['HS256'])
            return str(res.get("id"))

    def login_required(self, func):
        @wraps(func)
        def decorated_function(*args, **kws):
            if not 'Authorization' in request.headers:
                abort(401)

            user_id = None
            encode_token = request.headers['Authorization']
            try:
                user_id = jwt.decode(encode_token, api_secret, algorithms=['HS256'])
                # print(user_id)

            except:
                abort(401)

            return func(*args, **kws)

        return decorated_function


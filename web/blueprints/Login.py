from flask import Blueprint
from flask import request
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from flask import jsonify
from flask_api import status

Login = Blueprint('Login', __name__)


@Login.route('/Login', methods=['POST'])
def login():
    json = request.get_json()
    try:
        service = ServiceProvider().make_login_service()
        token = service.login_user(json)
        response = BaseResponse({"access token": token}, True, MessageIds.SUCCESS)
        return jsonify(response.serialize()), status.HTTP_201_CREATED

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST




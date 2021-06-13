from flask import Blueprint
from flask import request
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from flask import jsonify
from flask_api import status

ResetPassword = Blueprint('ResetPassword', __name__)


@ResetPassword.route('/ResetPassword/ShowQuestion', methods=['POST'])
def get_email():
    json = request.get_json()
    if "email" in json:
        email = json.get("email")
        try:
            service = ServiceProvider().make_reset_password_service()
            data = service.show_question(email)
            response = BaseResponse(data, True, MessageIds.ANSWER)
            return jsonify(response.serialize()), status.HTTP_201_CREATED

        except ValueError:
            response = BaseError(MessageIds.ERROR_WRONG_EMAIL_FROMAT)
            return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST

    response = BaseError(MessageIds.ERROR_INVALID_PROPERTY)
    return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST


@ResetPassword.route('/ResetPassword/ChangePassword', methods=['POST'])
def change_password():
    json = request.get_json()
    try:
        service = ServiceProvider().make_reset_password_service()
        result = service.change_password(json)
        response = BaseResponse(result, True, MessageIds.SUCCESS)
        return jsonify(response.serialize()), status.HTTP_201_CREATED

    except ValueError:
        response = BaseError(MessageIds.ERROR_WRONG_EMAIL_FROMAT)
        return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST




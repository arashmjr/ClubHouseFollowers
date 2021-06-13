from flask import Blueprint
from flask import request
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from flask import jsonify
from flask_api import status

Register = Blueprint('Register', __name__)


@Register.route('/Register', methods=['POST'])
def register():
    json = request.get_json()
    try:
        service = ServiceProvider().make_register_service()
        token = service.register_user(json)
        response = BaseResponse({"access token": token}, True, MessageIds.SUCCESS)
        return jsonify(response.serialize()), status.HTTP_201_CREATED

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST

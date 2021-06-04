from flask import Blueprint
from flask import request
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from flask import jsonify
from flask_api import status

SaveUser = Blueprint('SaveUser', __name__)

@SaveUser.route('/SaveUser', methods=['POST'])
def save_user():
    json = request.get_json()

    try:
        service = ServiceProvider().make_save_user_service()
        service.save_profile(json)
        response = BaseResponse({},True, MessageIds.SUCCESS)
        return jsonify(response.serialize()), status.HTTP_201_CREATED

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST






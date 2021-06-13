from flask import Blueprint
from flask import request
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from flask import jsonify
from flask_api import status
from seviceLayer.Managers.AuthorizationManager import AuthorizationManager

SaveUser = Blueprint('SaveUser', __name__)

authorize = AuthorizationManager()


@SaveUser.route('/SaveUser', methods=['POST'])
@authorize.login_required
def save_user():
    json = request.get_json()

    try:
        service = ServiceProvider().make_save_user_service()
        service.save_profile(json, request)
        response = BaseResponse({}, True, MessageIds.SUCCESS)
        return jsonify(response.serialize()), status.HTTP_201_CREATED

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST








from flask import Blueprint
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
from flask import jsonify
from flask import request
from flask_api import status

GetSuggestions = Blueprint('GetSuggestions', __name__)

authorize = AuthorizationManager()


@GetSuggestions.route('/GetSuggestions', methods=['GET'])
@authorize.login_required
def get_suggestions():
    try:
        service = ServiceProvider().make_get_suggestions_service()
        result = service.suggestion_user(request)
        response = BaseResponse(result, True, MessageIds.SUCCESS)
        return jsonify(response.serialize()), status.HTTP_201_CREATED

    except ValueError:
        response = BaseError(MessageIds.ERROR_NOT_FOUND)
        return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST



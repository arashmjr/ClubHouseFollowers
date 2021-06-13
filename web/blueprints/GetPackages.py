from flask import Blueprint
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from flask import jsonify
from flask import request
from flask_api import status
from seviceLayer.Managers.AuthorizationManager import AuthorizationManager

GetPackages = Blueprint('GetPackages', __name__)

authorize = AuthorizationManager()


@GetPackages.route('/GetPackages', methods=['GET'])
@authorize.login_required
def get_packages():
    try:
        service = ServiceProvider().make_get_packages_service()
        result = service.get_packages(request)
        response = BaseResponse(result, True, MessageIds.SUCCESS)
        return jsonify(response.serialize()), status.HTTP_201_CREATED
    except ValueError:
        response = BaseError(MessageIds.ERROR_NOT_FOUND)
        return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST




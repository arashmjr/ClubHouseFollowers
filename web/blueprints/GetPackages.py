from flask import Blueprint
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from flask import jsonify
from flask_api import status

GetPackages = Blueprint('GetPackages', __name__)


@GetPackages.route('/GetPackages', methods=['GET'])
def get_suggestions():
    try:
        service = ServiceProvider().make_get_packages_service()
        result = service.get_packages()
        response = BaseResponse(result, True, MessageIds.SUCCESS)
        return jsonify(response.serialize()), status.HTTP_201_CREATED
    except ValueError:
        response = BaseError(MessageIds.ERROR_NOT_FOUND)
        return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST



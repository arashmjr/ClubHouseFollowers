from flask import Blueprint
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from flask import jsonify
from flask_api import status

GetSuggestions = Blueprint('GetSuggestions', __name__)

@GetSuggestions.route('/GetSuggestions', methods=['GET'])
def get_suggestions():
    service = ServiceProvider().make_suggestions_service()
    service.suggetion_user()
    response = BaseResponse(True, MessageIds.SUCCESS)
    return jsonify(response.serialize()), status.HTTP_201_CREATED
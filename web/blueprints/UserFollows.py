from flask import Blueprint
from flask import request
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from flask import jsonify
from flask_api import status

UserFollows = Blueprint('UserFollows', __name__)

@UserFollows.route('/UserFollows', methods=['POST'])
def save_user():
    json = request.get_json()
    service = ServiceProvider().make_user_follow_service()
    service.save_user_follow(json)
    response = BaseResponse({}, True, MessageIds.SUCCESS)
    return jsonify(response.serialize()), status.HTTP_201_CREATED
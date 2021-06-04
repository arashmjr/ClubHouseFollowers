from flask import Blueprint
from seviceLayer.core.ServiceProvider import ServiceProvider
from web.dtos.BaseResponse import BaseError, BaseResponse
from web.utils.Localization import MessageIds
from flask import jsonify, request
from flask_api import status

Orders = Blueprint('Orders', __name__)

@Orders.route('/Orders', methods=['POST'])
def submit_orders():
    json = request.get_json()
    service = ServiceProvider().make_save_orders_service()
    result = service.save_orders(json)
    if result == True:
        response = BaseResponse({}, True, MessageIds.SUCCESS)
        return jsonify(response.serialize()), status.HTTP_201_CREATED

    response = BaseError(MessageIds.ERROR_INSUFFICIENT_ACCOUNT_BALANCE)
    return jsonify(response.serialize()), status.HTTP_400_BAD_REQUEST
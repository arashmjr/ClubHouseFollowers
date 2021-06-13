from repository.SaveOrderRepository import SaveOrderRepository
from repository.SaveUserRepository import SaveUserRepository
from Domain.models.SaveOrderDomainModel import SaveOrderDomainModel
from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
import datetime
from flask import Request


class SaveOrderService:
    order_repository: SaveOrderRepository
    save_user_repository: SaveUserRepository
    auth: AuthorizationManager

    def __init__(self, order_repository: SaveOrderRepository, save_user_repository: SaveUserRepository,
                 auth: AuthorizationManager):

        self.order_repository = order_repository
        self.save_user_repository = save_user_repository
        self.auth = auth

    def save_orders(self, json: str, request: Request):

        user_id = self.auth.extract_user_id(request)

        record = self.save_user_repository.find_record_by_user_id(user_id)

        if record is not None:
            if record['coin'] >= int(json['size']) * 2:
                isActive = True
                time = datetime.datetime.now()
                model = SaveOrderDomainModel(user_id, json['order_id'], json['size'], time, isActive)
                self.order_repository.insert(model)
                return True

        return False


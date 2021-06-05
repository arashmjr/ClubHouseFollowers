from repository.SaveOrderRepository import SaveOrderRepository
from repository.SaveUserRepository import SaveUserRepository
from Domain.models.SaveOrderDomainModel import SaveOrderDomainModel
import datetime


class SaveOrderService:
    order_repository: SaveOrderRepository
    save_user_repository: SaveUserRepository

    def __init__(self, order_repository: SaveOrderRepository, save_user_repository: SaveUserRepository):
        self.order_repository = order_repository
        self.save_user_repository = save_user_repository

    def save_orders(self, json: str):
        record = self.save_user_repository.find_record_by_user_id(json['user_id'])

        if record is not None:
            if record['coin'] >= int(json['size']) * 2:
                isActive = True
                time = datetime.datetime.now()
                model = SaveOrderDomainModel(json['user_id'], json['order_id'], json['size'], time, isActive)
                self.order_repository.insert(model)
                return True

        return False


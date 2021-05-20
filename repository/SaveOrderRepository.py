from pymongo.collection import ObjectId, Collection
from Domain.models.SaveOrderDomainModel import SaveOrderDomainModel


class SaveOrderRepository:
    collection: Collection

    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, model: SaveOrderDomainModel):
        self.collection.insert_one(model.to_dict())

    # def remove(self):
    #     x = self.collection.delete_many({})
    #
    # def find(self):
    #     for item in self.collection.find():
    #         print(item)
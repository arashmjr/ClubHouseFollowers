from pymongo.collection import ObjectId, Collection
from Domain.models.SaveOrderDomainModel import SaveOrderDomainModel


class SaveOrderRepository:
    collection: Collection

    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, model: SaveOrderDomainModel):
        result = self.collection.insert_one(model.to_dict())
        return str(result.inserted_id)

    def remove_all(self):
        delete_all = self.collection.delete_many({})
        print(delete_all.deleted_count, " documents deleted.")
        return delete_all

    def find(self):
        arr = []
        for item in self.collection.find():
            arr.append(item)
        return arr

    def find_suggestions(self):
        arr = []
        for item in self.collection.find({}, {"user_id": 1, "order_id": 1, "size": 1, "isActive": 1}):
             arr.append(item)
        return arr

    def find_record_by_user_id(self, user_id: str):
        return self.collection.find_one({"user_id": user_id})

    def update_isActive_field(self, document: dict):
        my_query = {"isActive": document['isActive']}
        new_values = {"$set": {"isActive": False}}
        return self.collection.update_one(my_query, new_values)
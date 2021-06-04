from pymongo.collection import ObjectId, Collection
from Domain.models import SaveUserDomainModel


class SaveUserRepository:
    collection: Collection

    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, model: SaveUserDomainModel):
        result = self.collection.insert_one(model.to_dict())
        return str(result.inserted_id)

    def find_record_by_user_id(self, user_id: str):
        return self.collection.find_one({"user_id": user_id})

    def get_all(self):
        arr = []
        for x in self.collection.find():
            arr.append(x)
        return arr

    def remove_record(self, user_id:  str):
        return self.collection.delete_one({'user_id': user_id})

    def remove_all(self):
        delete_all = self.collection.delete_many({})
        return delete_all

    def update_coins(self, document: dict):
        my_query = {"coin": document['coin']}
        new_values = {"$set": {"coin": document['coin'] + 1}}
        return self.collection.update_one(my_query, new_values)

    def find_suggestions_order(self, user_id: str):
        result = self.collection.find_one({"user_id": user_id}, {"user_id": 1,"name": 1, "photo_url": 1, "bio": 1})
        return result




from pymongo.collection import ObjectId, Collection
from Domain.models import SaveUserDomainModel


class SaveUserRepository:
    collection: Collection

    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, model: SaveUserDomainModel):
        self.collection.insert_one(model.to_dict())


    def find_record_by_user_id(self, user_id: str):
        return self.collection.find_one({"user_id": user_id})


    def remove_record(self, user_id:  str):
        return self.collection.delete_one({'user_id': user_id})




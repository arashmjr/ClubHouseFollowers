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

    def find(self):
        for x in self.collection.find():
            print(x)


    def remove_record(self, user_id:  str):
        return self.collection.delete_one({'user_id': user_id})

    def remove_all(self):
        return self.collection.delete_many({})

    def update_coins(self, document: dict):
        myquery = {"coin": document['coin']}
        newvalues = {"$set": {"coin": document['coin'] + 1}}
        return self.collection.update_one(myquery, newvalues)




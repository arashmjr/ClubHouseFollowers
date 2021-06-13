from pymongo.collection import ObjectId, Collection
from Domain.models.RegisterUserDomainModel import RegisterUserDomainModel
from pymongo import MongoClient
from bson.objectid import ObjectId


class VerificationRepository:
    collection: Collection

    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, model: RegisterUserDomainModel):
        result = self.collection.insert_one(model.to_dict())
        return str(result.inserted_id)

    def find_record_by_email(self, email: str):
        return self.collection.find_one({"email": email})

    def find_record_by_user_id(self, _id: str):
        return self.collection.find_one({"_id": ObjectId(_id)})

    def remove_all(self):
        delete_all = self.collection.delete_many({})
        print(delete_all)
        return delete_all

    def get_all(self):
        arr = []
        for x in self.collection.find():
            arr.append(x)
        return arr

    def update_password(self, record: dict, hashed_password):
        my_query = {"password": record['password']}
        new_values = {"$set": {"password": hashed_password}}
        return self.collection.update_one(my_query, new_values)


from pymongo.collection import ObjectId, Collection
from Domain.models.UserFollowDomainModel import UserFollowDomainModel

class UserFollowRepository:
    collection: Collection

    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, model: UserFollowDomainModel):
        self.collection.insert_one(model.to_dict())

    def find(self):
        for x in self.collection.find():
            print(x)

    def remove_all(self):
        return self.collection.delete_many({})



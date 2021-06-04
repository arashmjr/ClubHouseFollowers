from pymongo.collection import ObjectId, Collection
from Domain.models.UserFollowDomainModel import UserFollowDomainModel


class UserFollowRepository:
    collection: Collection

    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, model: UserFollowDomainModel):
        result = self.collection.insert_one(model.to_dict())
        return str(result.inserted_id)

    def find(self, user_id: str):
        arr = []
        for item in self.collection.find({"user_id": user_id}):
            arr.append(item)
        return arr

    def find_record_by_user_id(self, user_id: str):
        return self.collection.find_one({"user_id": user_id})

    def remove_all(self):
        delete_all = self.collection.delete_many({})
        print(delete_all.deleted_count, " documents deleted.")
        return delete_all

    def find_count_of_followIds(self, user_id: str, order_id: str):
        count = 0
        query = {"follow_id": user_id, "order_id": order_id}
        items = self.collection.find(query)
        if items is not None:
            for item in items:
                count = count + 1
            return count
        return None

    def find_record_by_followId_orderId(self, userID: str, user_id: str, order_id: str):

        query = {"user_id": userID, "follow_id": user_id, "order_id": order_id}
        result = self.collection.find(query)
        return result








from pymongo.collection import ObjectId, Collection

class SuggestionRepository:
    collection: Collection

    def __init__(self, collection: Collection):
        self.collection = collection

    def find_suggestions(self):
        for item in self.collection.find({}, {"user_id": 1, "photo_url": 1, "bio": 1}):
            print(item)

    def remove_record(self, user_id:  str):
        return self.collection.delete_one({'user_id': user_id})
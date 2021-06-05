from pymongo.collection import ObjectId, Collection
from Domain.models.GetPackagesDomainModel import GetPackagesDomainModel


class PackagesRepository:
    collection: Collection

    def __init__(self, collection: Collection):
        self.collection = collection

    def insert(self, model: GetPackagesDomainModel):
        result = self.collection.insert_one(model.to_dict())
        return str(result.inserted_id)

    def get_all(self):
        arr = []
        for item in self.collection.find():
            arr.append(item)
        return arr

    def remove_all(self):
        delete_all = self.collection.delete_many({})
        print(delete_all.deleted_count, " documents deleted.")
        return delete_all


import pymongo


class CoreDatabase:
    __instance = None
    __database_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=zlib&gssapiServiceName=mongodb")
    user_db = __database_client["user_db"]

    @staticmethod
    def get_instance():
        if CoreDatabase.__instance is None:
            CoreDatabase()
        return CoreDatabase.__instance

    def __init__(self):
        if CoreDatabase.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CoreDatabase.__instance = self

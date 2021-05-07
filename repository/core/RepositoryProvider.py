from repository.core.CoreDatabase import CoreDatabase
from repository.SaveUserRepository import SaveUserRepository

class RepositoryProvider:
    database = CoreDatabase.get_instance()

    def make_user_profile(self):
        collection = self.database.user_db["profile"]
        return SaveUserRepository(collection)


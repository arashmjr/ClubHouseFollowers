from repository.core.CoreDatabase import CoreDatabase
from repository.SaveUserRepository import SaveUserRepository
from repository.SuggestionRepository import SuggestionRepository
from repository.SaveOrderRepository import SaveOrderRepository

class RepositoryProvider:
    database = CoreDatabase.get_instance()

    def make_user_profile(self):
        collection = self.database.user_db["profile"]
        return SaveUserRepository(collection)

    def make_suggestions(self):
        collection = self.database.user_db["profile"]
        return SuggestionRepository(collection)

    def submit_orders(self):
        collection = self.database.user_db["orders"]
        return SaveOrderRepository(collection)
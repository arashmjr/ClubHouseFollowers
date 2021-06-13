from repository.core.CoreDatabase import CoreDatabase
from repository.SaveUserRepository import SaveUserRepository
from repository.SaveOrderRepository import SaveOrderRepository
from repository.UserFollowRepository import UserFollowRepository
from repository.PackagesRepository import PackagesRepository
from repository.VerificationRepository import VerificationRepository


class RepositoryProvider:
    database = CoreDatabase.get_instance()

    def make_authorization(self):
        collection = self.database.user_db["verification"]
        return VerificationRepository(collection)

    def make_user_profile(self):
        collection = self.database.user_db["profile"]
        return SaveUserRepository(collection)

    # def make_suggestions(self):
    #     collection = self.database.user_db["orders"]
    #     return SuggestionRepository(collection)

    def submit_orders(self):
        collection = self.database.user_db["orders"]
        return SaveOrderRepository(collection)

    def make_user_follows(self):
        collection = self.database.user_db["userFollow"]
        return UserFollowRepository(collection)

    def make_packages(self):
        collection = self.database.user_db["packages"]
        return PackagesRepository(collection)


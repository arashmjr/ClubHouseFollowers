from repository.core.RepositoryProvider import RepositoryProvider
from seviceLayer.SaveUserService import SaveUserService
from seviceLayer.SuggestionService import SuggestionService
from seviceLayer.SaveOrderService import SaveOrderService
from seviceLayer.UserFollowService import UserFollowService
from seviceLayer.Managers.AuthorizationManager import AuthorizationManager


class ServiceProvider:
    repository_provider: RepositoryProvider
    auth: AuthorizationManager

    def __init__(self):
        self.repository_provider = RepositoryProvider()
        self.auth = AuthorizationManager.get_instance()

    def make_authorization_manager(self):
        return self.auth

    def make_save_user_service(self):
        return SaveUserService(self.repository_provider.make_user_profile(),  self.auth)

    def make_suggestions_service(self):
        return SuggestionService(self.repository_provider.submit_orders(), self.repository_provider.make_user_follows(), self.repository_provider.make_user_profile())

    def make_save_orders_service(self):
        return SaveOrderService(self.repository_provider.submit_orders(), self.repository_provider.make_user_profile())

    def make_user_follow_service(self):
        return UserFollowService(self.repository_provider.make_user_follows(), self.repository_provider.make_user_profile())

from repository.core.RepositoryProvider import RepositoryProvider
from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
from seviceLayer.SaveUserService import SaveUserService


class ServiceProvider:
    repository_provider: RepositoryProvider
    auth: AuthorizationManager

    def __init__(self):
        self.auth = AuthorizationManager.get_instance()
        self.repository_provider = RepositoryProvider()

    def make_authorization_manager(self):
        return self.auth

    def make_save_user_service(self):
        return SaveUserService(self.repository_provider.make_user_profile(), self.auth)

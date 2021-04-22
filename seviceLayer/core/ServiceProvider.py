from repository.core.RepositoryProvider import RepositoryProvider
from seviceLayer.Managers.AuthorizationManager import AuthorizationManager

class ServiceProvider:
    repository_provider: RepositoryProvider
    auth: AuthorizationManager

    def __init__(self):
        self.auth = AuthorizationManager.get_instance()
        self.repository_provider = RepositoryProvider()

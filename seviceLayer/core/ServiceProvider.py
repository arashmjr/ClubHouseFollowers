from repository.core.RepositoryProvider import RepositoryProvider
from seviceLayer.SaveUserService import SaveUserService
from seviceLayer.SuggestionService import SuggestionService
from seviceLayer.SaveOrderService import SaveOrderService
from seviceLayer.UserFollowService import UserFollowService
from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
from seviceLayer.PackagesService import PackagesService
from seviceLayer.RegisterService import RegisterService
from seviceLayer.LoginService import LoginService
from seviceLayer.ResetPasswordService import ResetPasswordService


class ServiceProvider:
    repository_provider: RepositoryProvider
    auth: AuthorizationManager

    def __init__(self):
        self.repository_provider = RepositoryProvider()
        self.auth = AuthorizationManager()

    def make_authorization_manager(self):
        return self.auth

    def make_register_service(self):
        return RegisterService(self.repository_provider.make_authorization(), self.auth)

    def make_login_service(self):
        return LoginService(self.repository_provider.make_authorization(), self.auth)

    def make_reset_password_service(self):
        return ResetPasswordService(self.repository_provider.make_authorization(), self.auth)

    def make_save_user_service(self):
        return SaveUserService(self.repository_provider.make_user_profile(),  self.auth)

    def make_get_suggestions_service(self):
        return SuggestionService(self.repository_provider.submit_orders(), self.repository_provider.make_user_follows(),
                                 self.repository_provider.make_user_profile(), self.auth)

    def make_save_orders_service(self):
        return SaveOrderService(self.repository_provider.submit_orders(), self.repository_provider.make_user_profile(),
                                self.auth)

    def make_user_follow_service(self):
        return UserFollowService(self.repository_provider.make_user_follows(), self.repository_provider.make_user_profile(),
                                 self.auth)

    def make_get_packages_service(self):
        return PackagesService(self.repository_provider.make_user_profile(), self.repository_provider.make_packages(),
                               self.auth)





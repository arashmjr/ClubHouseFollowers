class AuthorizationManager:

    __instance = None

    def __init__(self):
        if AuthorizationManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AuthorizationManager.__instance = self

    @staticmethod
    def get_instance():
        if AuthorizationManager.__instance is None:
            AuthorizationManager()
        return AuthorizationManager.__instance
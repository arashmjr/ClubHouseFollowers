from flask import Flask
from .blueprints.SaveUser import SaveUser
from .blueprints.GetSuggestions import GetSuggestions
from .blueprints.Orders import Orders
from .blueprints.UserFollows import UserFollows
from .blueprints.GetPackages import GetPackages


class BaseRouter:
    base_url: str

    def __init__(self, base_url: str):
        self.base_url = base_url

    def register_flask_blueprints(self, app: Flask):
        # SaveUser.register(app, route_base=self.base_url)
        app.register_blueprint(SaveUser)
        app.register_blueprint(Orders)
        app.register_blueprint(UserFollows)
        app.register_blueprint(GetSuggestions)
        app.register_blueprint(GetPackages)







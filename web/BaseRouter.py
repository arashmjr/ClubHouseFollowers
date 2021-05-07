from flask import Flask
from .blueprints.SaveUser import SaveUser

class BaseRouter:
    base_url: str

    def __init__(self, base_url: str):
        self.base_url = base_url

    def register_flask_blueprints(self, app: Flask):
        # SaveUser.register(app, route_base=self.base_url)
        app.register_blueprint(SaveUser)




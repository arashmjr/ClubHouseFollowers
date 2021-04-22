from flask import Flask

class BaseRouter:
    base_url: str

    def __init__(self, base_url: str):
        self.base_url = base_url

    def register_flask_blueprints(self, app: Flask):
        pass
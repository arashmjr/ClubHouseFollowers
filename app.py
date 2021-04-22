from flask import Flask
from web.BaseRouter import BaseRouter

app = Flask(__name__)
base_url = '/'

router = BaseRouter(base_url)
router.register_flask_blueprints(app)

if __name__ == '__main__':
    app.run()

from flask import Flask, abort, request
from web.BaseRouter import BaseRouter
from functools import wraps
from config.config import api_secret
import jwt

app = Flask(__name__)
base_url = '/'

router = BaseRouter(base_url)
router.register_flask_blueprints(app)


# def authorize(f):
#     @wraps(f)
#     def decorated_function(*args, **kws):
#         if not 'Authorization' in request.headers:
#             abort(401)
#
#         user = None
#         data = request.headers['Authorization'].encode('ascii', 'ignore')
#         token = str.replace(str(data), 'Bearer ', '')
#         try:
#             user = jwt.decode(token, api_secret, algorithms=['HS256'])['sub']
#         except:
#             abort(401)
#
#         return f(user, *args, **kws)
#     return decorated_function


if __name__ == '__main__':
    app.run()

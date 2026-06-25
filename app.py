# Standard libraries
# /

# Third-party libraries
from flask import Flask, jsonify

# Local libraries
from config import Config
from src.app.app_helpers import app_users_get

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def users_get():
    return jsonify(doc for doc in app_users_get()), Config.HTTP_SUCCESS_CODE
# Standard libraries
import logging

# Third-party libraries
from flask import Flask, jsonify

# Local libraries
from config import Config
from src.app.app_helpers import app_users_get

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()])

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def users_get():
    return app_users_get(), Config.HTTP_SUCCESS_CODE
# Standard libraries
import logging

# Third-party libraries
from flask import Flask, jsonify

# Local libraries
from config import Config
from src.firestore.firestore_auth import initialize_firestore_app
from src.app.app_helpers import app_users_get

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()])

print(f'API Key starting with {Config.FIRESTORE_API_KEY[10]} retrieved from environment variables')
Config.firestore_client = initialize_firestore_app(Config.FIRESTORE_API_KEY)

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def users_get():
    return app_users_get(), Config.HTTP_SUCCESS_CODE
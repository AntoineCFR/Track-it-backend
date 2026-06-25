# Standard libraries
import logging
import tempfile

# Third-party libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Local libraries
# /

# Initiate logs
logger = logging.getLogger(__name__)

def initialize_firestore_app(firestore_secret):
    logger.info('Attempting to create JSON file for Firebase credentials...')
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as ff:
        ff.write(firestore_secret)
        firestore_secret_json = ff.name
    cred = credentials.Certificate(firestore_secret_json)
    logger.info(f'Trying to authenticate to Firebase using {firestore_secret_json}...')
    firebase_admin.initialize_app(cred)
    return firestore.client()
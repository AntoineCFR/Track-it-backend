# Standard libraries
import logging

# Third-party libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Local libraries
from config import Config

# Initiate logs
logger = logging.getLogger(__name__)

# Check authentication to Firebase and authenticate if not found
if not firebase_admin._apps:
    cred = credentials.Certificate(Config.FIRESTORE_SECRET)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

def get_firestore_documents_from_collection(collection):
    ''' Function description

    Args: 

    Returns:
    '''
    docs = db.collection(collection).stream()
    for doc in docs:
        logger.info(f"{doc.id} => {doc.to_dict()}")
    return 1

def firestore_helpers_main():
    get_firestore_documents_from_collection('users')
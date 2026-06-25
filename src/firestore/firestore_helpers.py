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

def get_firestore_documents_from_collection(collection):
    ''' Function description

    Args: 

    Returns:
    '''
    logger.info('Now trying to stream collection from Firestore...')
    docs = Config.firestore_client.collection(collection).stream()
    for doc in docs:
        logger.info(f"{doc.id} => {doc.to_dict()}")
    return 1
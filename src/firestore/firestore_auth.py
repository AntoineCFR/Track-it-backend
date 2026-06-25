# Standard libraries
import logging
import json

# Third-party libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Local libraries
# /

# Initiate logs
logger = logging.getLogger(__name__)

def initialize_firestore_app(firestore_secret):
    print('I WAS HERE !!!!!!!!!')
    if not firestore_secret:
        print('I WAS ALSO HERE !!!!!!!!!')
        logger.error("FIRESTORE_SECRET empty or missing.")
        raise ValueError(
            "Could not retrieve FIRESTORE_SECRET from system files."
        )
    cred = credentials.Certificate(firestore_secret)
    logger.info(f'Trying to authenticate to Firebase using JSON...')
    firebase_admin.initialize_app(cred)
    return firestore.client()

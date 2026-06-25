# Standard libraries
import os
import logging

# Third-party libraries
# /

# Local libraries
from src.firestore.firestore_auth import initialize_firestore_app

# Initiate logs
logger = logging.getLogger(__name__)
logger.info('Reading config file...')

class Config:
    
    # Firestore credentials
    firestore_client = initialize_firestore_app(os.getenv('FIRESTORE_SECRET'))

    # Firestore table info
    FIRESTORE_USERS_COLLECTION = 'users'

    # HTTP status codes
    HTTP_SUCCESS_CODE = 200
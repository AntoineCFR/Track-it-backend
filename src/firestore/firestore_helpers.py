# Standard libraries
# /

# Third-party libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Local libraries
from config import Config

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
    return docs
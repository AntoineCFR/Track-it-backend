# Standard libraries
# /

# Third-party libraries
# /

# Local libraries
from config import Config
from src.firestore.firestore_helpers import get_firestore_documents_from_collection

def app_users_get():
    # Get users collection from Firestore helper
    return(get_firestore_documents_from_collection(Config.FIRESTORE_USERS_COLLECTION))
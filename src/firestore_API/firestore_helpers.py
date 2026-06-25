# Get Firestore credentials

# Standard libraries
# /

# Third-party libraries
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Local libraries
# /

def get_firestore_credentials(api_key):
    ''' Function description

    Args: 

    Returns:
    '''
    # Use a service account.
    cred = credentials.Certificate(api_key)

    app = firebase_admin.initialize_app(cred)

    db = firestore.client()

    return(db)


def get_firestore_documents_from_collection(db, collection):

    docs = db.collection(collection).stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

def firestore_main(api_key):
    get_firestore_credentials(api_key)
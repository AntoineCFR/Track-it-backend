# Standard libraries
import os

# Third-party libraries
# /

# Local libraries
# /

print('Reading config file...')

class Config:
    
    # Firestore credentials
    FIRESTORE_API_KEY = os.getenv('FIRESTORE_SECRET')
    firestore_client = None

    # Firestore table info
    FIRESTORE_USERS_COLLECTION = 'users'

    # HTTP status codes
    HTTP_SUCCESS_CODE = 200
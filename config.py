# Standard libraries
import os

# Third-party libraries
# /

# Local libraries
# /

class Config:
    
    # Environment variables
    FIRESTORE_SECRET = os.getenv('FIRESTORE_SECRET')

    # Firestore table info
    FIRESTORE_USERS_COLLECTION = 'users'

    # HTTP status codes
    HTTP_SUCCESS_CODE = 200
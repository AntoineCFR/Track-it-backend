# Standard libraries
import os
import tempfile
import json

# Third-party libraries
# /

# Local libraries
# /

class Config:
    
    # Environment variables
    firestore_secret_json = os.getenv('FIRESTORE_SECRET')
    if firestore_secret_json:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as ff:
            ff.write(firestore_secret_json)
            FIRESTORE_SECRET = ff.name

    # Firestore table info
    FIRESTORE_USERS_COLLECTION = 'users'

    # HTTP status codes
    HTTP_SUCCESS_CODE = 200
# Standard libraries
# /

# Third-party libraries
# /

# Local libraries
# /

print('Reading config file...')

class Config:
    
    # Firestore credentials path
    GOOGLE_APPLICATION_CREDENTIALS = '/etc/secrets/FIRESTORE_SECRET'
    firestore_client = None

    # Firestore table info
    FIRESTORE_USERS_COLLECTION = 'users'

    # HTTP status codes
    HTTP_SUCCESS_CODE = 200
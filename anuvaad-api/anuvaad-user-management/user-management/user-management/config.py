import os
import time

DEBUG = False
API_URL_PREFIX = "/v1/users"
HOST = '0.0.0.0'
PORT = 5001

ENABLE_CORS = False

#folders and file path
# download_folder = 'upload'


# BLOCK_TYPES = [{'key':'lines'},{'key':'images'},{'key':'tables'},{'key':'text_blocks'}]



# new mongo config
MONGO_DB_HOST   = os.environ.get('MONGO_IP', 'localhost')
MONGO_DB_PORT   = os.environ.get('MONGO_PORT', 27017)
MONGO_DB_SCHEMA = os.environ.get('user-management')

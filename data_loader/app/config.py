import os


MONGO_URL = os.getenv('MONGO_URL')
DATABASE_NAME = os.getenv('DATABASE_NAME')
TRACKS_COLLECTION_NAME = os.getenv('TRACKS_COLLECTION_NAME')

QUEUE_URL = os.getenv('QUEUE_URL')
QUEUE_ROUTING_KEY = os.getenv('QUEUE_ROUTING_KEY')

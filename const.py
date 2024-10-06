import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class CosmosDBConfig():
    def __init__(self):
        self.uri = os.getenv('COSMOS_DB_ENDPOINT', '')
        self.key = os.getenv('COSMOS_DB_KEY', '')
        self.database_name = os.getenv('COSMOS_DB_DATABASE', '')
        self.container_name = os.getenv('COSMOS_DB_CONTAINER', '')

    def get_connection_info(self):
        return {
            'COSMOS_DB_ENDPOINT': self.uri,
            'COSMOS_DB_KEY': self.key,
            'COSMOS_DB_DATABASE_NAME': self.database_name,
            'COSMOS_DB_CONTAINER_NAME': self.container_name
        }

COSMOSDB_CONFIG = CosmosDBConfig()
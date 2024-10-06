import asyncio
from azure.cosmos import exceptions, CosmosClient, PartitionKey
from dotenv import load_dotenv
import os
from const import COSMOSDB_CONFIG

# Load environment variables from .env file
client = CosmosClient(COSMOSDB_CONFIG.uri, COSMOSDB_CONFIG.key)
database = client.get_database_client(COSMOSDB_CONFIG.database_name)
container = database.get_container_client(COSMOSDB_CONFIG.container_name)

# Function to zero pad a number
def zero_pad_number(number, width):
    return str(number).zfill(width)

# Create 1000 items in the container in bulk
batch_size = 1000
items = []

# Generate 1000 items
for i in range(1, batch_size + 1):
    padded_id = zero_pad_number(i, 5)
    item = {
        'id': padded_id,
    }
    
    for j in range(1, 10000):
        item[f'message{j}'] = f'This is Sample Data {padded_id}'
    
    items.append(item)

async def create_item(item):
    try:
        container.create_item(body=item)
    except exceptions.CosmosHttpResponseError as e:
        print(f'An error occurred: {e}')

async def main():
    tasks = [create_item(item) for item in items]
    await asyncio.gather(*tasks)
    print(f'{batch_size} items have been created in the container.')

if __name__ == "__main__":
    print(f'starting to create {batch_size} items in the container...')
    asyncio.run(main()) 
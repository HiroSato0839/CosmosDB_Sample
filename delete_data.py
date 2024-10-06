from azure.cosmos import CosmosClient, exceptions
from const import COSMOSDB_CONFIG 

# Initialize the Cosmos client
client = CosmosClient(COSMOSDB_CONFIG.uri, COSMOSDB_CONFIG.key)

# Get the database and container
database = client.get_database_client(COSMOSDB_CONFIG.database_name)
container = database.get_container_client(COSMOSDB_CONFIG.container_name)



# Delete all items in the container
for item in container.query_items(query='SELECT * FROM c', enable_cross_partition_query=True):
    if( 'id' in item):
        id  = str(item['id'])
        container.delete_item(item, partition_key=id)

print("All items have been deleted.")
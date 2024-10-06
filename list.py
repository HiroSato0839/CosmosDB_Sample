import os
from azure.cosmos import CosmosClient, exceptions
from dotenv import load_dotenv
from const import COSMOSDB_CONFIG

# .envファイルから環境変数を読み込む
load_dotenv()

# Cosmos DBクライアントを作成
client = CosmosClient(COSMOSDB_CONFIG.uri, COSMOSDB_CONFIG.key)

# データベースとコンテナを指定
database = client.get_database_client(COSMOSDB_CONFIG.database_name)
container = database.get_container_client(COSMOSDB_CONFIG.container_name)

# データをクエリして一覧表示
def list_items():
    try:
        items = container.read_all_items()
        print(items)
    except exceptions.CosmosHttpResponseError as e:
        print(f'エラーが発生しました: {e.message}')

if __name__ == "__main__":
    list_items()
    print("データの一覧を表示しました。")
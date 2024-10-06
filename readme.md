# Cosmos DB Sample

CosmosDB の RU 消費量のログ検証用に作ったスクリプトたち

## 動作環境

python 3.11.1

## 使用ライブラリ

- python-dotenv
- azure-cosmos

## 利用方法

1. .env ファイルを以下のフォーマットで用意する

```
COSMOS_DB_URI=<your-cosmos-db-uri>
COSMOS_DB_PRIMARY_KEY=<your-cosmos-db-primary-key>
COSMOS_DB_DATABASE_ID=<your-database-id>
COSMOS_DB_CONTAINER_ID=<your-container-id>
```

2. python <利用したいファイル名>.py で実行

## ファイル説明

| ファイル名                     | 説明                                           |
| ------------------------------ | ---------------------------------------------- |
| `const.py`                     | 定数用ファイル（主に DB の接続情報取得で利用） |
| `create_data`                  | データを CosmosDB に投入するスクリプト         |
| `data_ingedelete_datastion.py` | データを CosmosDB から削除するスクリプト       |
| `list.py`                      | データの一覧を CosmosDB から取得するスクリプト |

## 注意（免責事項）

- このコードは現状のまま提供されており、明示的または黙示的な保証は一切ありません。
- 使用に伴うリスクはすべてユーザーが負うものとします。
- 著者または著作権者は、コードの使用に起因するいかなる損害についても責任を負いません。

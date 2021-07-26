from pymongo import MongoClient
import pandas as pd
import json


def seed_database(mongo_url, db_name):

    client = MongoClient(mongo_url)

    database = client[db_name]
    collection = database['books50']
    books_df = pd.read_csv('books_50.csv')
    books_df['isbn13'] = books_df['isbn13'].astype(str)
    books_json = books_df.to_json(orient='records',
                                  indent=3,
                                  storage_options=dict)

    collection.insert_many(json.loads(books_json))

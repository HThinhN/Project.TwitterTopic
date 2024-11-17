from settings import *
import pandas as pd
from pymongo import MongoClient

class MongoDB: 
    def __init__(self):
        # Connect to mongodb
        self.client = MongoClient(MONGODB_ADDR)
        self.db = self.client[CLIENT_NAME]
        self.collection = self.db[DATABASE_NAME]

        # Read csv by pandas
        self.df = pd.read_csv(TWEETS_DATA_PATH)

    def run(self): 
        # Insert data into mongodb
        data = self.df.to_dict(orient="records")
        self.collection.insert_many(data)

        print(f"Inserted {len(data)} records into MongoDB")
from settings import *
from pymongo import MongoClient
from kafka import KafkaProducer
import json

class Producer: 
    def __init__(self): 
        # Connect to mongodb
        self.client = MongoClient(MONGODB_ADDR)
        self.db = self.client[CLIENT_NAME]
        self.collection = self.db[DATABASE_NAME]
        # Connect to kafka
        self.producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    # Get data from MongoDB
    def get_data_from_mongodb(self):
        cursor = self.collection.find({})
        for document in cursor:
            # Remove _id field (ObjectId)
            if '_id' in document:
                document.pop('_id')

            self.producer.send(KAFKA_TOPIC, document)
            print(f"Sent: {document}")

    def run(self):
        self.get_data_from_mongodb()

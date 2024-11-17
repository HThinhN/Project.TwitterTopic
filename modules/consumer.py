from settings import *
from kafka import KafkaConsumer
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
import json

class Consumer: 
    def __init__(self): 
        # Create SparkSession
        self.spark = SparkSession.builder \
            .appName("KafkaSparkStreaming") \
            .getOrCreate()
        
        # Connect to Kafka Consumer
        self.consumer = KafkaConsumer(KAFKA_TOPIC, 
                                bootstrap_servers=BOOTSTRAP_SERVERS,
                                value_deserializer=lambda v: json.loads(v.decode('utf-8')))
        
    # Pull data from Kafka Broker and handle by Spark Streaming
    def process_streaming_data(self):
        for message in self.consumer:
            record = message.value

            # Show data 
            df = self.spark.createDataFrame([record])

            df.show()

    def run(self): 
        self.process_streaming_data()

from init import *
from modules.mongodb import MongoDB
from modules.producer import Producer
from modules.consumer import Consumer
from modules.sentiment_analysis import Sentiment_Analysis

def main():
    print("======= Menu =======")
    print("1. MongoDB: Insert data into MongoDB")
    print("2. Producer: Send data to Broker")
    print("3. Consumer: Receive data from Broker")
    print("4. Sentiment Analysis: Sentiment analysis from tweets ")
    opt = int(input("=> Enter your option: "))

    # 1. MongoDB: Insert data into MongoDB
    if (opt == 1):
        mongodb = MongoDB()
        mongodb.run() 
        print("MongoDB - Finished")

    # 2. Producer: Send data to Broker
    elif (opt == 2): 
        producer = Producer()
        producer.run()
        print("Producer - Finished")

    # 3. Consumer: Receive data from Broker
    elif (opt == 3):
        consumer = Consumer()
        consumer.run()
        print("Consumer - Finished")

    # 4. Sentiment Analysis: Sentiment analysis from tweets 
    elif (opt == 4):
        # raw_data = ["I hate using this product, it's so bad!"]
        sentiment_analysis = Sentiment_Analysis()
        sentiment_analysis.train_model()
        sentiment_analysis.run()
        print("Sentiment Analysis - Finished")
    
    else: 
        pass


if __name__ == "__main__":
    main()
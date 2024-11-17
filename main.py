from init import *
from modules.mongodb import MongoDB
from modules.producer import Producer
from modules.consumer import Consumer

def main():
    opt = int(input("=> Enter your option: "))
    print("======= Menu =======")
    print("1. MongoDB: Insert data into MongoDB")
    print("2. Producer: Send data to Broker")
    print("3. Consumer: Receive data from Broker")


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
    
    else: 
        pass


if __name__ == "__main__":
    main()
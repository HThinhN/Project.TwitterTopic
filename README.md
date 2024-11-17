# Project: TwitterTopic
This project was implemented to perform sentiment analysis on tweets continuously in the real time by using Kafka to stream tweets 
to Apache Spark and from that, the analytic results will be visualized by Plotly. 

## 0. Individual introduction:
| Full Name                  |   Student's ID   | Student's Email                    |      Individual Email              |
|:--------------------------:|:----------------:|:----------------------------------:|:----------------------------------:|
| Nguyễn Hoàng Thịnh         |  20120587        | 20120587@student.hcmus.edu.vn      | hoangthinh130322@gmail.com               |

## 1. Used tools:
+ ***Programming:*** Python
+ ***Technique:***

## 2. MongoDB: 
Store tweets data into MongoDB

### Init MongoDB: 

    sudo systemctl start mongod 

## 3. Kafka: 

### Init Kafka: 
#### Init Zookeeper: 
    
    zookeeper-server-start.sh kafka/config/zookeeper.properties

#### Init Kafkaserver

    kafka-server-start.sh kafka/config/server.properties

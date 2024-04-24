from kafka import KafkaConsumer
from pymongo import MongoClient
import json

def store_results_in_database(topic, MongoDB, collection_name):
    client = MongoClient('localhost', 27017)
    db = client[database_name]
    collection = db[collection_name]

    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    for message in consumer:
        data = message.value
        # Store data in MongoDB
        collection.insert_one(data)
        print("Data stored in MongoDB:", data)

# Example usage
if __name__ == "__main__":
    store_results_in_database('amazon_data_topic', 'amazon_db', 'amazon_collection')

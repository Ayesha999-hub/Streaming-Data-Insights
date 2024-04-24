from kafka import KafkaConsumer
import json
import time

def apriori_consumer(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    
    for message in consumer:
        data = message.value
        # Implement Apriori algorithm here
        print("Apriori insights:", data)
        time.sleep(0.5)  # Simulate processing time

# Example usage
if __name__ == "__main__":
    apriori_consumer('amazon_data_topic')

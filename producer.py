from kafka import KafkaProducer
import json
import time

def stream_data("c:c/amazon_fashion", topic):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    
    # Read preprocessed data and stream it
    with open(input_file, 'r') as f:
        data = json.load(f)
        for item in data:
            producer.send(topic, value=item)
            time.sleep(0.1)  # Simulate real-time streaming


if __name__ == "__main__":
    stream_data('data/preprocessed_data.json', 'amazon_data_topic')

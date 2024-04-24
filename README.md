# Streaming-Data-Insights
Preprocessing:
The preprocessing step involves loading the sampled Amazon dataset, cleaning and formatting it for analysis, and generating a new JSON file containing the preprocessed data. We have implemented a preprocessing script (preprocessing.py) that reads the sampled_amazon_metadata.json file, extracts relevant information such as product titles and categories, and saves the preprocessed data to a new JSON file (preprocessed_data.json). This ensures that the data is in a suitable format for further analysis.

Streaming Pipeline Setup:
The streaming pipeline consists of a producer application that streams the preprocessed data in real-time and three consumer applications that subscribe to the producer's data stream. The producer script (streaming_producer.py) reads the preprocessed data and streams it to a Kafka topic. The consumers include one for Apriori algorithm (streaming_consumer_apriori.py), one for PCY algorithm (similar structure), and one for custom analysis (streaming_consumer_custom.py). These consumers process the data stream and print real-time insights and associations.

Frequent Itemset Mining:
The Apriori algorithm is implemented in one consumer (streaming_consumer_apriori.py). It scans the data stream, identifies frequent itemsets, and prints real-time insights and associations. Similarly, the PCY algorithm is implemented in another consumer. Both algorithms handle the challenge of streaming data by employing techniques such as sliding window approach and approximation techniques to adapt to the streaming environment.

Database Integration:
Database integration is achieved using MongoDB. Each consumer is modified to connect to MongoDB and store the results. The database_integration script (database_integration.py) connects each consumer to MongoDB and stores the processed data in a database named amazon_db and collection named amazon_collection.

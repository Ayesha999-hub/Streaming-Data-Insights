import json

def preprocess_data("c:c/amazon_fashion", output_file):
    # Load the sampled Amazon dataset
    with open(input_file, 'r') as f:
        data = json.load(f)
    
  
        preprocessed_data = [{'title': item.get('title', ''), 'categories': item.get('categories', [])} for item in data]
    
    # Write preprocessed data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(preprocessed_data, f)

if __name__ == "__main__":
    preprocess_data('data/sampled_amazon_metadata.json', 'data/preprocessed_data.json')

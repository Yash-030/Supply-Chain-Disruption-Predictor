import json

# Load data from JSON file
with open("event_registry_data.json", "r") as file:
    data = json.load(file)

# Extract and display key details
articles = data.get("articles", {}).get("results", [])
for article in articles:
    print(f"Title: {article['title']}")
    print(f"Source: {article['source']['title']}")
    print(f"Published Date: {article['date']}")
    print(f"URL: {article['url']}")
    print("-" * 40)

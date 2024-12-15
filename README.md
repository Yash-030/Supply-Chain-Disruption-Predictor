1. Load and Display Articles from a JSON File
This script reads article data from a JSON file named event_registry_data.json. It extracts key details, such as the title, source, publication date, and URL of each article, and displays them in a clean and readable format. It’s helpful for quickly reviewing stored article data.

2. Fetch Articles from Event Registry API and Save to File
This script connects to the Event Registry API using a provided API key and retrieves articles based on a specific keyword. It saves the response, including the article details, into a local JSON file called event_registry_data.json. This is useful for collecting and storing article data for further analysis.

3. Fetch, Save, and Display Articles
This script combines the functionality of fetching articles from the Event Registry API, saving the data to a JSON file, and then displaying the key details (title, source, date, and URL) for each article. It ensures that data is both stored and presented in a user-friendly way.

General Use Cases
Data Analysis: Collect and inspect article data for trends or insights.
News Aggregation: Automatically fetch and organize news based on specific topics or keywords.
Offline Storage: Save data locally for future processing or sharing.
Requirements
Python installed on your system.
Access to the Event Registry API (API key required).
The requests and json Python modules.
How to Use
Replace the placeholder API_KEY in the scripts with your Event Registry API key.
Run the scripts to fetch or process article data.
View or analyze the output, either saved in event_registry_data.json or displayed in the console.

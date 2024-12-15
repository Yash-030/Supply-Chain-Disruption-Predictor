# AI-Driven Supply Chain Disruption Predictor and Inventory Optimization System

## **News Article Fetcher**

This program fetches news articles from the Event Registry API based on specific keywords and saves the results to a JSON file.

### **How It Works**
1. The program uses the provided API key to connect to the Event Registry API.
2. It searches for articles that match the specified keywords.
3. The retrieved articles are saved in a file called `event_registry_data.json`.

### **Requirements**
- Python installed on your system.
- The `requests` and `json` Python libraries.
- An API key from the Event Registry platform.

### **Usage**
1. Replace the placeholder `API_KEY` in the script with your Event Registry API key.
2. Specify the desired keyword(s) in the `params` section of the script.
3. Run the program. If successful:
   - The matching articles will be saved to a file named `event_registry_data.json`.

### **Output**
The program generates a JSON file containing:
- Article titles
- Sources
- Publication dates
- URLs

---

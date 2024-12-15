## **1. fetch_data**
This program connects to the Event Registry API to fetch article data based on specific keywords. The fetched data is saved to a JSON file named `event_registry_data.json`. 

### **What It Does:**
- Sends a request to the API using the provided API key and keyword(s).
- Retrieves article details, such as the title, source, publication date, and URL.
- Saves the API response in a structured JSON format for offline use.

### **Use Case:**
Use this program to collect and store article data from the Event Registry API for further analysis.

---

## **2. parse_data**
This program reads the JSON file (`event_registry_data.json`) created by **fetch_data** and extracts key information from the articles. It displays the details in a user-friendly format.

### **What It Does:**
- Opens the saved JSON file.
- Extracts important details for each article, including:
  - Article title
  - Source name
  - Publication date
  - URL
- Displays the extracted details in the console.

### **Use Case:**
Use this program to review and understand the article data stored in the JSON file.

---

## **3. fetch_parse_data**
This program combines the functionality of **fetch_data** and **parse_data**. It fetches article data from the Event Registry API, saves it to a JSON file, and immediately displays the key details of the articles.

### **What It Does:**
- Fetches article data from the API based on specified keywords.
- Saves the response to a JSON file (`event_registry_data.json`).
- Extracts and displays key article details like title, source, publication date, and URL.

### **Use Case:**
Use this program when you need to both fetch new article data and view the details in a single step.

---

### **General Use Cases for All Programs**
- **Data Analysis**: Gather and analyze news articles for trends or insights.
- **News Aggregation**: Automatically fetch and display news articles on specific topics.
- **Offline Storage**: Save article data locally for future reference or processing.

### **How to Use**
1. Ensure Python is installed on your system.
2. Install the required Python modules (`requests` and `json`).
3. Replace the placeholder `API_KEY` in the programs with your Event Registry API key.
4. Run the desired program based on your needs:
   - Use **fetch_data** to fetch and save article data.
   - Use **parse_data** to extract and view details from the saved JSON file.
   - Use **fetch_parse_data** for a combined fetch-and-view workflow.

---

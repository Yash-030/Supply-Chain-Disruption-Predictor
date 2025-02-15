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
## Milestone-2
## **LLM.py: Supply Chain Risk and Sentiment Analysis**

### **Overview**
The `LLM.py` script leverages OpenAI's GPT-3.5-Turbo and Hugging Face's transformers library to perform detailed analysis of news articles related to supply chain disruptions. The script focuses on identifying risks and analyzing sentiment to provide actionable insights. It works seamlessly with `fetch_data.py`, which retrieves news articles from the Event Registry API.

---

### **Features**
1. **Supply Chain Risk Analysis**:
   - Uses OpenAI's GPT-3.5-Turbo model to analyze the body of articles for potential risks in the supply chain.
   - Provides insights into vulnerabilities such as disruptions, resource shortages, geopolitical issues, and economic factors.

2. **Sentiment Analysis**:
   - Uses Hugging Face's `pipeline` for sentiment analysis with the `distilbert-base-uncased-finetuned-sst-2-english` model.
   - Determines whether the tone of the article is positive, negative, or neutral.

3. **Integration with `fetch_data.py`**:
   - Processes JSON data generated by the `fetch_data.py` script, enabling seamless integration.
   - Automatically reads and analyzes news articles from `event_registry_data.json`.

4. **Customizable**:
   - Easily adaptable to analyze other types of data or domains by modifying input files or pipeline settings.

---

### **How It Works**
1. **Input**:
   - Reads articles from a JSON file (`event_registry_data.json`) generated by `fetch_data.py`.
   - Extracts the title and body of each article for analysis.

2. **Analysis**:
   - GPT-3.5-Turbo identifies specific risks mentioned in the article and summarizes them.
   - Sentiment analysis identifies the overall tone of the article.

3. **Output**:
   - Displays risk analysis and sentiment results for each article on the console.

---

### **Semiconductor Supply Chain Risk Factors**
The script is particularly effective in analyzing risks within semiconductor supply chains. Common risks include:
- **Geopolitical Tensions**: Trade restrictions, embargoes, or conflicts impacting major semiconductor producers (e.g., Taiwan, China).
- **Raw Material Shortages**: Limited availability of critical materials like silicon, rare earth metals, and gallium.
- **Logistics Disruptions**: Delays in shipping, port congestion, and transportation bottlenecks.
- **Economic Factors**: Currency fluctuations, inflation, or shifts in consumer demand.
- **Technological Dependencies**: High reliance on advanced manufacturing technologies concentrated in specific regions.
- **Natural Disasters**: Earthquakes, typhoons, and other events affecting production hubs.
- **Cybersecurity Threats**: Increasing vulnerability of supply chain systems to cyberattacks.

---
## Milestone-3
## Semiconductor Supply Chain Analysis

The program, **warehouse.py**, analyzes semiconductor supply chain data to generate actionable alerts based on utilization rates, risk analysis, and sentiment analysis. It assists in making proactive decisions for supply chain management by categorizing actions into **SELL**, **BUY**, and **MONITOR** based on specific conditions.

### Program Workflow

1. **Input Data**:
   - The program reads data from a CSV file named `semiconductor_supply_chain_data_updated.csv`.
   - Each row includes information such as monthly incoming stock, warehouse capacity, risk analysis levels, and sentiment scores.

2. **Calculations**:
   - **Utilization Rate**: Calculated as `Monthly Incoming / Warehouse Capacity`.
   - Thresholds are defined as follows:
     - **High utilization**: >70%
     - **Low utilization**: <40%
   - Alerts are generated based on utilization, risk levels, and sentiment.

3. **Alert Generation**:
   - **SELL**: Triggered if utilization is high, risk is high, and sentiment is negative.
   - **MONITOR**: Triggered for high utilization but neutral or positive sentiment.
   - **BUY**: Triggered if utilization is very low (<40%).

4. **Output**:
   - Alerts are displayed in the terminal for immediate review.
   - Alerts are saved to a new CSV file named `supply_chain_alerts.csv` for documentation or further analysis.

---
Certainly! Here's the focused explanation about the **email alerting** feature and the working of the code in **Milestone-4**:

---

### **Milestone-4**  
**Warehouse Alert System with Email Notification**

The program, `email_alert.py`, analyzes semiconductor supply chain data and generates alerts based on the current utilization, risk levels, and sentiment of the supply chain. It helps stakeholders take quick action (such as buying, selling, or monitoring) to avoid potential disruptions and optimize inventory management.

---

### **Program Workflow**

**Input Data:**
- The program reads data from a CSV file (`semiconductor_supply_chain_data_updated.csv`).
- The data includes:
  - Monthly incoming stock.
  - Warehouse capacity.
  - Risk analysis levels (Low, Medium, High).
  - Sentiment analysis (Positive, Neutral, Negative).
  - 
### **Email Alerting Process**

1. **Email Notification**:
   - After generating the alerts, the system identifies the **most recent month** in the data.
   - Alerts related to this **latest month** are prepared for email delivery.

2. **Email Content**:
   - The email contains:
     - The **Month** of the alert.
     - The **Action** to be taken (SELL, MONITOR, BUY).
     - The **Reason** for the action (e.g., high utilization, risk, and sentiment).

3. **Sending the Email**:
   - The email is sent via Gmail’s SMTP server.
   - The program connects to the server, logs in with the sender’s credentials, and sends the email to the recipient.
   - The email includes all the details of the recent alerts, providing stakeholders with a clear understanding of what actions need to be taken in response to the supply chain status.

4. **Outcome**:
   - The alerts are displayed in the terminal for immediate review.
   - The most recent alerts are sent to the recipient’s email for proactive supply chain management.
   - The received email will looks like this.
<img width="730" alt="Example_Email" src="https://github.com/user-attachments/assets/4868b8e7-8ebc-45c3-af4b-32fb240ef5ef" />

---

### **Key Features of Email Alerting in Milestone-4:**
- **Real-Time Alerts**: Stakeholders receive immediate email notifications with the most recent supply chain alerts.
- **Automated Communication**: No manual intervention is needed for alert dissemination; the system automatically sends the email with the most up-to-date information.
- **Actionable Insights**: Each email contains specific actions (SELL, MONITOR, BUY) based on the data, helping stakeholders make informed decisions quickly.

---



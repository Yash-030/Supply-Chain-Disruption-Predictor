import pandas as pd

def analyze_semiconductor_supply_chain(file_path):
    # Load the CSV data
    data = pd.read_csv(file_path)

    # Define thresholds and conditions
    supply_threshold = 0.7  # 70% supply utilization is considered high
    risk_threshold = "High"  # Risk levels: Low, Medium, High
    sentiment_threshold = "Negative"  # Sentiment: Positive, Neutral, Negative

    alerts = []

    for index, row in data.iterrows():
        # Calculate supply utilization (equivalent to warehouse utilization)
        utilization = row['Monthly Incoming'] / row['Warehouse Capacity']

        # Analyze risk factors and sentiment
        if utilization > supply_threshold or row['Risk Analysis'] == risk_threshold:
            if row['Sentiment'] == sentiment_threshold:
                # Create an alert if utilization is high and sentiment is negative
                alerts.append((row['Month'], "SELL", f"High utilization ({utilization:.2f}), {row['Risk Analysis']} risk, {row['Sentiment']} sentiment"))
            else:
                # Monitor if utilization is high, but sentiment is neutral or positive
                alerts.append((row['Month'], "MONITOR", f"High utilization ({utilization:.2f}) with {row['Risk Analysis']} risk"))
        elif utilization < 0.4:  # If utilization is very low, trigger a BUY alert
            alerts.append((row['Month'], "BUY", f"Low utilization ({utilization:.2f}), consider buying semiconductor components"))

    return alerts

# Sample CSV data creation for Semiconductor Supply Chain Example
data = {
    'Month': ['January', 'February', 'March'],
    'Warehouse Capacity': [10000, 10000, 10000],
    'Monthly Incoming': [8500, 6000, 3000],
    'Monthly Outgoing': [8000, 7000, 2500],
    'Risk Analysis': ['Medium', 'High', 'Low'],
    'Sentiment': ['Neutral', 'Negative', 'Positive']
}

# Save sample data to CSV for demonstration
sample_file = "semiconductor_supply_chain_data.csv"
pd.DataFrame(data).to_csv(sample_file, index=False)

# Analyze the semiconductor supply chain data
alerts = analyze_semiconductor_supply_chain(sample_file)

# Display alerts
for alert in alerts:
    print(f"Month: {alert[0]}, Action: {alert[1]}, Reason: {alert[2]}")
import pandas as pd

def analyze_semiconductor_supply_chain(file_path):
    # Load the CSV data
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please provide a valid file path.")
        return []

    # Define thresholds and conditions
    supply_threshold = 0.7  # 70% supply utilization is considered high
    risk_threshold = "High"  # Risk levels: Low, Medium, High
    sentiment_threshold = "Negative"  # Sentiment: Positive, Neutral, Negative

    alerts = []

    for index, row in data.iterrows():
        # Calculate supply utilization (equivalent to warehouse utilization)
        utilization = row['Monthly Incoming'] / row['Warehouse Capacity']

        # Analyze risk factors and sentiment
        if utilization > supply_threshold or row['Risk Analysis'] == risk_threshold:
            if row['Sentiment'] == sentiment_threshold:
                # Create an alert if utilization is high and sentiment is negative
                alerts.append((row['Month'], "SELL", f"High utilization ({utilization:.2f}), {row['Risk Analysis']} risk, {row['Sentiment']} sentiment"))
            else:
                # Monitor if utilization is high, but sentiment is neutral or positive
                alerts.append((row['Month'], "MONITOR", f"High utilization ({utilization:.2f}) with {row['Risk Analysis']} risk"))
        elif utilization < 0.4:  # If utilization is very low, trigger a BUY alert
            alerts.append((row['Month'], "BUY", f"Low utilization ({utilization:.2f}), consider buying semiconductor components"))

    return alerts

# File path for the semiconductor supply chain data
file_path = "C:/Users/91630/OneDrive/Desktop/Milestone-3/semiconductor_supply_chain_data_updated.csv"

# Analyze the semiconductor supply chain data
alerts = analyze_semiconductor_supply_chain(file_path)

# Display alerts
if alerts:
    for alert in alerts:
        print(f"Month: {alert[0]}, Action: {alert[1]}, Reason: {alert[2]}")
else:
    print("No alerts generated or file not found.")

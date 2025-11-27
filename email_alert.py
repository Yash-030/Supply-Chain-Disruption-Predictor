import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Function to analyze the supply chain data and generate alerts
def analyze_semiconductor_supply_chain(file_path):
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please provide a valid file path.")
        return [], None

    # Define thresholds and conditions
    supply_threshold = 0.7  # 70% supply utilization is considered high
    risk_threshold = "High"  # Risk levels: Low, Medium, High
    sentiment_threshold = "Negative"  # Sentiment: Positive, Neutral, Negative

    alerts = []

    for index, row in data.iterrows():
        # Calculate supply utilization (equivalent to warehouse utilization)
        utilization = row['Monthly Incoming'] / row['Warehouse Capacity']

        # Analyze risk factors and sentiment
        alert_statement = ""  # Variable to hold the additional statement for each alert

        if utilization > supply_threshold or row['Risk Analysis'] == risk_threshold:
            if row['Sentiment'] == sentiment_threshold:
                # Create an alert if utilization is high and sentiment is negative
                alert_statement = "\nDue to high utilization and negative sentiment, we recommend selling to avoid further risks."
                alerts.append((row['Month'], "SELL", f"High utilization ({utilization:.2f}), {row['Risk Analysis']} risk, {row['Sentiment']} sentiment. {alert_statement}"))
            else:
                # Monitor if utilization is high, but sentiment is neutral or positive
                alert_statement = "\nThe utilization is high, but sentiment is neutral/positive. Consider monitoring the situation closely."
                alerts.append((row['Month'], "MONITOR", f"High utilization ({utilization:.2f}) with {row['Risk Analysis']} risk. {alert_statement}"))
        elif utilization < 0.4:  # If utilization is very low, trigger a BUY alert
            alert_statement = "\nThe incoming stock is low, but considering the high risk and outgoing stock, it is advisable to buy as much as possible to mitigate risks."
            alerts.append((row['Month'], "BUY", f"Low utilization ({utilization:.2f}), consider buying semiconductor components. {alert_statement}"))

    return alerts, data

# Function to filter alerts for the most recent month
def get_most_recent_month_alerts(alerts, data):
    # Find the most recent month in the data
    latest_month = data['Month'].iloc[-1]  # Assumes data is ordered chronologically
    # Filter alerts for the latest month
    recent_alerts = [alert for alert in alerts if alert[0] == latest_month]
    return recent_alerts

# Function to send email
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Create a MIME object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main script
if __name__ == "__main__":
    # File path for the supply chain data
    file_path = "semiconductor_supply_chain_data_updated.csv"

    # Analyze the supply chain data
    alerts, data = analyze_semiconductor_supply_chain(file_path)

    # Get recent month alerts
    if data is not None:
        recent_alerts = get_most_recent_month_alerts(alerts, data)

        # Prepare email details
        sender_email = ""
        sender_password = ""
        recipient_email = ""

        # Send recent alerts via email
        if recent_alerts:
            alert_messages = "\n\n".join(
                [f"Month: {alert[0]}\nAction: {alert[1]}\nReason: {alert[2]}" for alert in recent_alerts]
            )
            send_email(
                sender_email=sender_email,
                sender_password=sender_password,
                recipient_email=recipient_email,
                subject="Warehouse Alert",
                body=f"Alert for the most recent month:\n\n{alert_messages}"
            )
        else:
            print("No alerts generated for the recent month, no email sent.")


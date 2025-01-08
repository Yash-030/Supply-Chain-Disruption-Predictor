import openai
from transformers import pipeline
import json

# OpenAI API key
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

# Initializing sentiment analysis pipeline
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Loading articles from a JSON file
def load_articles_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            articles = json.load(file)
        return articles
    except Exception as e:
        print(f"Error loading JSON file: {str(e)}")
        return []

def analyze_article(title, body):
    print(f"\nAnalyzing article: {title}")
    
    # Risk Analysis with OpenAI
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI that analyzes supply chain risks."},
                {"role": "user", "content": f"Analyze the following article for risks:\n\n{body[:2000]}"}  # Truncate to 2000 characters for OpenAI API
            ]
        )
        risk_analysis = response['choices'][0]['message']['content']
    except Exception as e:
        risk_analysis = f"Error in risk analysis: {str(e)}"
    
    print(f"\nRisk Analysis:\n{risk_analysis}")

    # Sentiment Analysis with Hugging Face
    try:
        sentiment = sentiment_analyzer(body[:512])  # Truncate to 512 tokens
    except Exception as e:
        sentiment = [{"label": "UNKNOWN", "score": 0.0}]
    
    print(f"\nSentiment Analysis:\n{sentiment}")

def main():
    # Providing the path to local JSON file
    file_path = 'event_registry_data.json'  
    articles = load_articles_from_json(file_path)
    
    # Printing the structure of the loaded data for debugging
    print(json.dumps(articles, indent=4))  

    # Checking if articles key exists and process the results
    if isinstance(articles, dict) and 'articles' in articles and 'results' in articles['articles']:
        for article in articles['articles']['results']:  # Access the articles in 'results'
            if isinstance(article, dict) and 'title' in article and 'body' in article:
                analyze_article(article['title'], article['body'])
            else:
                print("Invalid article structure:", article)
    else:
        print("No valid articles found.")

if __name__ == "__main__":
    main()

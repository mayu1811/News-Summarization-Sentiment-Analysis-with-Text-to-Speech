import pandas as pd

def comparative_analysis(news_articles):
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for article in news_articles:
        sentiment_counts[article["sentiment"]] += 1
    
    df = pd.DataFrame(sentiment_counts.items(), columns=["Sentiment", "Count"])
    return df

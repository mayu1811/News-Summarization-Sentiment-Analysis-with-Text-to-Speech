from fastapi import FastAPI
from news_scraper import scrape_news
from sentiment_analysis import analyze_sentiment
from comparative_analysis import comparative_analysis
from text_to_speech import text_to_speech

app = FastAPI()

@app.get("/analyze/{company}")
def analyze_news(company: str):
    articles = scrape_news(company)
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["title"])
    
    sentiment_report = comparative_analysis(articles)
    summary = f"Positive: {sentiment_report.iloc[0]['Count']}, Negative: {sentiment_report.iloc[1]['Count']}, Neutral: {sentiment_report.iloc[2]['Count']}"
    
    tts_file = text_to_speech(summary)
    
    return {"articles": articles, "summary": summary, "tts_file": tts_file}


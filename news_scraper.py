import requests
from bs4 import BeautifulSoup

def scrape_news(company):
    search_url = f"https://news.google.com/search?q={company}&hl=en-US&gl=US&ceid=US:en"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    
    for index, item in enumerate(soup.select("article")[:10]):   
        
        title_element = item.select_one("a.JtKRv") 
        title = title_element.text.strip() if title_element else "No Title"
        
        link_element = title_element  
        link = f"https://news.google.com{link_element['href'][1:]}" if link_element and 'href' in link_element.attrs else "No Link"

        articles.append({"title": title, "link": link})
    
    return articles


import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze/"

st.title("📢 News Summarization & Sentiment Analysis")
st.subheader("Enter a company name to get a structured sentiment report")

company = st.text_input("Company Name")

if st.button("Analyze News"):
    if company:
        with st.spinner("Fetching and analyzing news..."):
            response = requests.get(API_URL + company)
            if response.status_code == 200:
                data = response.json()
                
                st.write("### Sentiment Analysis Summary")
                st.write(data["summary"])
                
                st.write("### News Articles")
                for article in data["articles"]:
                    st.write(f"**Title:** {article['title']}")
                    st.write(f"**Sentiment:** {article['sentiment']}")
                    st.write(f"[Read More]({article['link']})")

                st.write("### Listen to Summary")
                st.audio("output.mp3")
            else:
                st.error("Error fetching news")

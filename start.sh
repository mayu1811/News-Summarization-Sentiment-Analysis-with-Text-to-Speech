#!/bin/bash

# Start FastAPI with Uvicorn
nohup uvicorn api:app --reload &

# Start Streamlit
streamlit run app.py

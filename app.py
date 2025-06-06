import streamlit as st
from textblob import TextBlob  # Example sentiment tool

st.title("Sentiment Analysis Dashboard")

# Input text area
user_input = st.text_area("Enter text to analyze sentiment:")

if st.button("Analyze"):
    if user_input:
        analysis = TextBlob(user_input)
        sentiment_score = analysis.sentiment.polarity
        
        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score == 0:
            sentiment = "Neutral"
        else:
            sentiment = "Negative"
        
        st.write(f"Sentiment: **{sentiment}**")
        st.write(f"Sentiment Score: {sentiment_score:.2f}")
    else:
        st.write("Please enter some text for analysis.")

# based on the words you're learning,
# it would give you more information to help your learning
# other meanings, conjugatation, example sentence in context

import streamlit as st
import requests

API_URL = "http://localhost:8000/explain/"

st.title("Leximate - Word Explanation")

# Input box to enter a new word
word = st.text_input("Enter a word you want to learn")

# Button to get explanation for the word
if st.button("Get Explanation"):
    if word:
        request_endpoint = f"{API_URL}{word}"
        st.write(f"Requesting explanation for '{word}'... at {request_endpoint}")
        response = requests.get(request_endpoint)
        st.write(f"This was the response {response}, with data {response.json()}")
        if response.status_code == 200:
            data = response.json()
            explanation = data.get("explanation", "No explanation found.")
            st.write(f"**Word:** {data.get('word')}")
            st.write(f"**Explanation:** {explanation}")
        else:
            st.error("Failed to retrieve explanation. Please check the FastAPI server.")
    else:
        st.error("Please enter a word.")
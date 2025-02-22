import streamlit as st
import requests
from rag_backend.rag_logic import query_index
from config import LLM_API_ENDPOINT

st.title("LLM with RAG Front-end")

query = st.text_input("Enter your query:")

if st.button("Submit"):
    if query:
        #RAG Query
        rag_response = query_index(query)
        st.write("RAG Response:", rag_response)

        #Direct LLM API Query (optional)
        try:
            response = requests.post(LLM_API_ENDPOINT, json={"prompt": query})
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            llm_response = response.json()
            st.write("LLM API Response:", llm_response)
        except requests.exceptions.RequestException as e:
            st.error(f"Error querying LLM API: {e}")

    else:
        st.warning("Please enter a query.")
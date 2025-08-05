import streamlit as st
import json
import pandas as pd

# Load chat logs from the JSON file
def load_logs():
    try:
        with open("chat_logs.json", "r") as f:
            data = [json.loads(line) for line in f]
        return pd.DataFrame(data)
    except FileNotFoundError:
        return pd.DataFrame(columns=["timestamp", "user_input", "bot_response", "topic", "rating"])

# Load the data into a DataFrame
df = load_logs()

# Streamlit app setup
st.set_page_config(page_title="Chatbot Analytics", layout="wide")
st.title("🤖 Chatbot Analytics Dashboard")

# If data is empty, show a warning
if df.empty:
    st.warning("No chat logs found yet.")
else:
    # Total number of queries
    st.metric("📊 Total Queries", len(df))

    # Most common topics
    st.subheader("📌 Most Common Topics")
    st.bar_chart(df["topic"].value_counts())

    # User satisfaction ratings (1 to 5)
    if "rating" in df and df["rating"].notna().any():
        st.subheader("⭐ User Ratings")
        st.bar_chart(df["rating"].value_counts().sort_index())

    # Recent chat logs table
    st.subheader("🧾 Recent Interactions")
    st.dataframe(df.sort_values("timestamp", ascending=False).head(10))

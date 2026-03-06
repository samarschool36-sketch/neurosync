import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="NeuroSync",
    layout="wide"
)

st.title("🧠 NeuroSync - Cognitive Support Companion")

# Load HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display the HTML app
components.html(html_code, height=1000, scrolling=True)

import streamlit as st

st.set_page_config(
    page_title="About Me",
    page_icon="🧑‍💼",
)

# Set the title of the page
st.title("About Me")

# Add a welcome message
st.header("Welcome to My AI Journey")

# Introduction
st.write("""
I'm from Govtech, and am a participant in the AI Champions Bootcamp Pilot. This program has provided me with valuable skills in Generative AI and Large Language Models (LLMs).
""")

# What I Learned section
st.subheader("What I Learned")
st.write("""
During the bootcamp, I focused on:
1. **Using Large Language Models & Prompt Engineering**: Learning how to create effective prompts to utilize LLMs.
2. **Building Custom LLM Pipelines**: Developing AI solutions tailored to specific business needs and workflows.
3. **Creating Proof-of-Concept (PoC) Apps**: Using frameworks like Langchain, Crew.AI, and Streamlit to develop practical applications.
""")

# My Project section
st.subheader("My Project")
st.write("""
In the final month, I applied these skills to develop a proof-of-concept app aimed at improving my day to day processes. This project demonstrates the practical use of AI in synthesizing information from different sources.
""")

# Looking Ahead section
st.subheader("Looking Ahead")
st.write("""
I plan to continue exploring AI technologies and using them in my current role. The AI Champions Bootcamp Pilot has given me practical experience and provided new insights into how it should be applied to my day to day work.

Thank you for visiting my page.
""")

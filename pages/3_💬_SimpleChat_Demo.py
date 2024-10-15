import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

st.set_page_config(page_title="Simple Chat Demo", page_icon="💬")

st.markdown("# Simple Chat Demo")
st.sidebar.header("Simple Chat Demo")

# Load the OpenAI API key from the .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_key = ""

client = OpenAI(api_key=openai_api_key)

# Sidebar input for OpenAI API key
api_key_input = st.sidebar.text_input("Enter OpenAI API Key", value=openai_api_key, type="password")

# Store the API key in session state
if api_key_input:
    st.session_state["openai_api_key"] = api_key_input

# Initialize OpenAI client with the API key from session state
if "openai_api_key" in st.session_state:
    client = OpenAI(api_key=st.session_state["openai_api_key"])
else:
    st.error("Please enter your OpenAI API key in the sidebar.")

st.title("Chat Application")
st.write("This is a simple chat application using the OpenAI API.")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Clear the input box
    st.text_input("You:", value="", key="user_input")
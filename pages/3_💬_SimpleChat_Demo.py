import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from utility import check_password


st.set_page_config(page_title="Simple Chat Demo", page_icon="💬")

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# endregion <--------- Streamlit Page Configuration --------->

st.markdown("# Simple Chat Demo")
st.sidebar.header("Simple Chat Demo")

# Load OpenAI API key
load_dotenv()  
openai_api_key = os.getenv("KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

client = OpenAI(
    api_key=openai_api_key,
    base_url="https://litellm.govtext.gov.sg/",
    default_headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0"},
)

st.title("Chat Application")
st.write("This is a simple chat application using the OpenAI API.")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-prd-gcc2-lb"

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
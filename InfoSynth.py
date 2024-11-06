import streamlit as st
from utility import check_password

st.set_page_config(
    page_title="Welcome to the InfoSynth (proof of concept)",
    page_icon="👋",
)

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# endregion <--------- Streamlit Page Configuration --------->

st.write("# Welcome to the InfoSynth (proof of concept)! 👋")

with st.expander("Disclaimer"):
    st.write('''
        IMPORTANT NOTICE: This web application is developed as a proof-of-concept prototype. The information provided here is NOT intended for actual usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.
        Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.
        Always consult with qualified professionals for accurate and personalized advice.
    ''')
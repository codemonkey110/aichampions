import streamlit as st
from utility import check_password

st.set_page_config(
    page_title="Methodology",
    page_icon="🛠️",
)

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# endregion <--------- Streamlit Page Configuration --------->

# Set the title of the page
st.title("Methodology for Creating a Proof of Concept (PoC) with a Multi-PDF LLM")

# Define Objectives and Use Cases
st.subheader("1. Define Objectives and Use Cases")
st.write("""
- **Objective**: Improving the synthesis of information from multiple pdfs with a focus on identifying and reducing friction when integrating the new with existing workflows.
- **Use Cases**: Identify specific use cases where the LLM can add value. Examples include:
  - Automating document review and analysis.
  - Enhancing risk assessment with integrated data sources.
  - Extracting insights from financial reports and visual data.
""")

# Data Collection and Preparation
st.subheader("2. Data Collection and Preparation")
st.write("""
- **Data Sources**: Gather relevant data from various sources.
- **Data Cleaning**: Ensure the data is clean, well-organized, and annotated if necessary.
- **Data Integration**: Combine the different documents into a cohesive dataset.
""")

# Model Selection and Customization
st.subheader("3. Model Selection and Customization")
st.write("""
- **Model Selection**: Choose a suitable LLM framework.
- **Customization**: Basic Fine-tuning of the selected model on the specific dataset to improve its performance on the defined use cases.
""")

# Development of PoC Application
st.subheader("4. Development of PoC Application")
st.write("""
- **Workflow Breakdown**: Breakdown the workflow into likely steps that minimizes friction for achieving outcomes required for day to day work.
- **Framework Selection**: Choose a development framework such as Langchain, Crew.AI, or Streamlit for building the PoC application.
- **Application Design**: Design the application interface and workflow. Ensure it is user-friendly and meets the needs of the end-users.
- **Integration**: Integrate the respective workflows into the application. This includes uploading the PDFs, ingesting the PDFs, and ensuring smooth interaction between different components.
""")

# Testing and Validation
st.subheader("5. Testing and Validation")
st.write("""
- **Testing**: Conduct thorough testing of the PoC application. This includes functional testing, performance testing, and user acceptance testing.
- **Validation**: Validate the results produced by the application. Ensure the outputs are accurate, relevant, and useful for the defined use cases.
""")

# Feedback and Iteration
st.subheader("6. Feedback and Iteration")
st.write("""
- **User Feedback**: Gather feedback from end-users and stakeholders. Identify any issues or areas for improvement.
- **Iteration**: Iterate on the PoC based on feedback. Make necessary adjustments to improve the application’s performance and usability.
""")

# Documentation and Presentation
st.subheader("7. Documentation and Presentation")
st.write("""
- **Documentation**: Document the entire process, including methodology, data sources, model selection, and results.
""")

# Deployment and Scaling (Optional)
st.subheader("8. Deployment and Scaling (Tentative)")
st.write("""
- **Deployment**: If the PoC is successful, determine the best means to operationalize it for day to day work 
""")

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
st.title("Methodology for drafting of Tender Response using CrewAI")

# Define Objectives and Use Cases
st.write('''
        
        While the initial intent was to explore the use of CrewAI to audit the Tender Process, due to the difficulty in sourcing for sample data for the end to end tender process, it was decided to first work on a project that creates the sample data instead.
        Using a document sourced online to set the scene, the **Tender Response Preparation Crew** is an AI-driven team structured to prepare a  response for a tender. This crew is specifically designed to handle complex, multi-agent tasks by breaking down the tender response process into manageable components, each overseen by a specialized agent.
        Multiple agents (use cases) were configured to handle different aspects of the tender response, such as requirements analysis, project planning, cost breakdown, and compliance verification. The crew is managed by a Tender Response Manager, who ensures coordination and synchronization across agents to deliver a high-quality response.

        #### Background and Purpose
        The purpose of the crew is to coordinate and deliver a cohesive tender response for a project on "structural setup and management of multimedia projection" for an annual event, the "Light to Night Singapore" festival, hosted by the National Gallery Singapore. The tender document requires detailed project planning, budget breakdowns, technical responses, and compliance adherence. Each agent in this crew plays a distinct role, focusing on specific requirements such as cost analysis, project planning, and compliance verification, all coordinated by a Tender Response Manager.

        #### Implementation Overview
        1. **Crew Composition**:
        - The crew comprises five agents: **Tender Response Manager**, **Requirements Manager**, **Technical Writer**, **Cost Analyst** and **Compliance Specialist**.
        - Each agent has a tailored role, goal, and backstory aligned with their function in the tender preparation process.

        2. **Agent Responsibilities**:
        - **Tender Response Manager**:
            - Central coordinator, ensuring all tasks align with the overarching response strategy, quality standards, and timeline.
        - **Requirements Manager**:
            - Understands the tender requirements and evaluate the key deliverables and evaluation criteria.             
        - **Technical Writer**:
            - Drafts high-quality written content for each tender section, including detailed project plans and compliance statements.
        - **Cost Analyst**:
            - Develops a detailed and competitive cost breakdown, adhering to the tender’s pricing structure.
        - **Compliance Specialist**:
            - Reviews all requirements to ensure that each document, certification, and form meets the tender specifications.

        3. **Task Workflow**:
        - **Hierarchical Process**: Tasks are configured to execute hierarchically in response to requested tasks.
            - **Tender Requirements Analysis**
            - **Project Plan Drafting** 
            - **Cost Breakdown Preparation** 
            - **Compliance Verification**

        4. **Kickoff Execution**:
        - The crew is initiated with the `kickoff()` method, which include the Tender Document to allow agents to access the document as they work through the tasks.
        This crew setup enables a structured, multi-agent approach to responding to queries from the user on preparing a competitive, compliant, and professionally written tender response. 
        - The Tender Response Manager ensures synchronization across agents, while specialized agents provide expertise on cost, compliance, and technical documentation, ultimately delivering a high-quality response for the tender.
             
        #### Instructions
        - **Input Prompt**: Enter a query "Please prepare a draft of the Tender Response".
        - **Output**: The crew will generate a detailed response based on the input prompt, showcasing the collaborative efforts of the agents in preparing a comprehensive tender response. (Observe the conversation the crew is having in the notifications. This may take some time.)
    
        #### Issues/Improvements
        - Unable to configure CrewAI Tool - PDFSearchTool to use AMF Embedder for RAG.
        - Occasionally the response doesn't get printed out on completion. If so, re-run by prompting it for the response.
    ''')

# Add a download button for the file
with open("./data/Tender_Document.pdf", "rb") as file:
    btn = st.download_button(
        label="Download Tender Document",
        data=file,
        file_name="Tender_Document.pdf",
        mime="application/pdf"
    )

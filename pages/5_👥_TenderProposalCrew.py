import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Crew, Agent, Task, LLM
from crewai.process import Process
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.agents import AgentAction, AgentFinish
from langchain_openai import ChatOpenAI
from typing import Any, Dict
from utility import check_password

st.set_page_config(page_title="Tender Proposal Crew", page_icon="👥")

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# endregion <--------- Streamlit Page Configuration --------->

st.markdown("# Tender Proposal Crew")

with st.expander("Background"):
    st.write('''
        The **Tender Response Preparation Crew** is an AI-driven team structured to prepare a thorough and competitive response for a large-scale tender. This crew is specifically designed to handle complex, multi-agent tasks by breaking down the tender response process into manageable components, each overseen by a specialized agent.

        ### Background and Purpose
        The purpose of the crew is to coordinate and deliver a cohesive tender response for a project on "structural setup and management of multimedia projection" for an annual event, the "Light to Night Singapore" festival, hosted by the National Gallery Singapore. The tender document requires detailed project planning, budget breakdowns, technical responses, and compliance adherence. Each agent in this crew plays a distinct role, focusing on specific requirements such as cost analysis, project planning, and compliance verification, all coordinated by a Tender Response Manager.

        ### Implementation Overview
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
    ''')
    # Add a download button for the file
    with open("./data/Tender_Document.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Tender Document",
            data=file,
            file_name="Tender_Document.pdf",
            mime="application/pdf"
        )

# Load OpenAI API key
load_dotenv()  
openai_api_key = os.getenv("KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

# Initialize OpenAI client with the API key
client = LLM(
    model="gpt-4o",  # Use the standard OpenAI model name
    api_key=openai_api_key,
    base_url="https://litellm.govtext.gov.sg/",
    default_headers={
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0"
    },
    custom_llm_provider="azure openai",
    deployment_id="gpt-4o-prd-gcc2-lb"  # Your Azure deployment name
)

# Define agents with their specific roles and goals

# Tender Response Manager Agent
tender_response_manager = Agent(
    role="tender response manager",
    goal=f"""Coordinate and oversee the activities of all agents involved in the tender response preparation.
         Ensure that each agent's output aligns with the overall strategy and quality standards of the response.""",
    backstory=f"""With a wealth of experience managing high-stakes projects, you excel at orchestrating collaborative teams. 
              Known for your keen eye for detail and strategic oversight, you ensure that every component of the tender response is cohesive, accurate, and tailored to meet client expectations. Your ability to swiftly address challenges and maintain team synergy makes you an invaluable leader in complex, multi-agent projects.""",
    llm=client,
    verbose=True
)

# Requirements Manager Agent
requirements_manager = Agent(
    role="requirements manager",
    goal="To understand the tender requirements and evaluate the key deliverables and evaluation criteria.",
    backstory=(
        "You are an experienced requirements manager specializing in managing large-scale event tenders. "
        "You excel at being able to condense the key deliverables and evaluation criteria of tender documents."
    ),
    llm=client,
    verbose=True
)

# Technical Writer Agent
technical_writer = Agent(
    role="technical writer",
    goal="Draft detailed, clear, and professional responses for each section of the tender, including project plans and compliance statements.",
    backstory=(
        "With expertise in crafting high-quality, clear documentation, you excel at translating technical specifications "
        "into accessible, professional language suited for tender submissions."
    ),
    llm=client,
    verbose=True
)

# Cost Analyst Agent
cost_analyst = Agent(
    role="cost analyst",
    goal="Develop a detailed and competitive cost breakdown for the tender response, aligning with the tender’s pricing structure.",
    backstory=(
        "You have a strong background in budgeting and financial planning, especially for event logistics. "
        "You focus on creating cost-effective proposals that meet compliance standards."
    ),
    llm=client,
    verbose=True
)

# Compliance Specialist Agent
compliance_specialist = Agent(
    role="compliance specialist",
    goal="Ensure all tender requirements, certifications, and documentation are thoroughly reviewed and completed.",
    backstory=(
        "Your background in contract law and regulatory compliance enables you to verify tender documentation meticulously, "
        "ensuring full compliance with the specifications."
    ),
    llm=client,
    verbose=True
)

# Initialize the message log in session state if not already present
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What would you like the crew to do?"}]

# Display existing messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Define tasks for each agent

    # Task: Tender Response Manager Analysis
    tender_response_task = Task(
        description=f"""Consider how you would go about the task, '{prompt}'.
                    Create a plan to complete the task.
                    The final step should always be a response relevant to the initial query""",
        expected_output="A detailed plan for the team to complete the task.",
        agent=tender_response_manager
    )

    # Task: Tender Requirements Analysis
    requirements_analysis_task = Task(
        description=f"""Analyze the Requirement Specifications (Section B) and Evaluation Criteria (Section C) of the tender document.
                    Identify key deliverables and evaluation priorities to shape the tender response.""",
        expected_output="A list of key requirements and evaluation criteria, with notes on addressing each in the response.",
        agent=requirements_manager
    )

    # Task: Project Plan Drafting
    project_plan_task = Task(
        description=(
            "Develop a draft project plan based on the Scope of Work and Project Milestones in the tender document. "
            "The plan should cover setup, testing, operation, and teardown phases."
        ),
        expected_output="A comprehensive project timeline with detailed descriptions of each phase.",
        agent=technical_writer
    )

    # Task: Cost Breakdown Preparation
    cost_breakdown_task = Task(
        description=(
            "Use Annex B to prepare a detailed cost proposal, ensuring alignment with the pricing structure in the tender. "
            "Include optional costs and justify each cost item for transparency."
        ),
        expected_output="A complete cost table with explanations, covering base and optional costs.",
        agent=cost_analyst
    )

    # Task: Compliance Verification
    compliance_verification_task = Task(
        description=(
            "Review the tender requirements to ensure all necessary forms, certifications, and track record documents are included. "
            "Confirm compliance with each specified criterion."
        ),
        expected_output="A compliance checklist with corresponding documentation as per the tender’s submission requirements.",
        agent=compliance_specialist
    )
    
    # Set up the crew and process tasks sequentially
    tender_response_crew = Crew(
        agents=[tender_response_manager, requirements_manager, technical_writer, cost_analyst, compliance_specialist],
        tasks=[
            tender_response_task,
            requirements_analysis_task,
            project_plan_task,
            cost_breakdown_task,
            compliance_verification_task
        ],
        #process=Process.sequential,
        process=Process.hierarchical,
        manager_llm=client,
        full_output=True,
        verbose=True
    )
    
    final = tender_response_crew.kickoff(inputs={'tender_document_path': '../data/Tender_Document.pdf'})

    # Display the final result
    result = f"## Here is the Final Result \n\n {final}"
    st.session_state.messages.append({"role": "assistant", "content": result})
    st.chat_message("assistant").write(result)
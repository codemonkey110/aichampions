import os
import streamlit as st
import sys
from dotenv import load_dotenv
from crewai import Crew, LLM, Process
from crew_agents import CrewAgents, StreamToExpander
from crew_tasks import CrewTasks

from utility import check_password

st.set_page_config(page_title="Tender Proposal Crew", page_icon="👥")

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# endregion <--------- Streamlit Page Configuration --------->

class TenderCrew:

    def __init__(self, client, prompt):
        self.client = client
        self.prompt = prompt
        self.output_placeholder = st.empty()

    def run(self):
        agents = CrewAgents()
        tasks = CrewTasks()   

        tender_response_agent = agents.tender_response_agent(self.client)
        requirements_manager_agent = agents.requirements_agent(self.client)
        technical_writer_agent = agents.technical_writer_agent(self.client)
        cost_analyst_agent = agents.cost_analyst_agent(self.client)
        compliance_specialist_agent = agents.compliance_specialist_agent(self.client)

        tender_response_task = tasks.tender_response_task(tender_response_agent, self.prompt)
        requirements_analysis_task = tasks.requirements_analysis_task(requirements_manager_agent, self.prompt)
        project_plan_task = tasks.project_plan_task(technical_writer_agent, self.prompt)
        cost_analysis_task = tasks.cost_analysis_task(cost_analyst_agent, self.prompt)
        compliance_analysis_task = tasks.compliance_analysis_task(compliance_specialist_agent, self.prompt)

        crew = Crew(
            agents=[
                tender_response_agent, requirements_manager_agent, technical_writer_agent, cost_analyst_agent, compliance_specialist_agent
            ],
            tasks=[tender_response_task, requirements_analysis_task, project_plan_task, cost_analysis_task, compliance_analysis_task],
            process=Process.hierarchical,
            manager_llm = client,
            verbose=True
        )

        result = crew.kickoff()
        self.output_placeholder.markdown(result)

        return result

st.markdown("# Tender Proposal Crew")

# Load OpenAI API key
load_dotenv()  
openai_api_key = os.getenv("KEY")
os.environ["AZURE_OPENAI_API_KEY"] = openai_api_key
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://litellm.govtext.gov.sg/"


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

# Initialize the message log in session state if not already present
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What would you like the Tender Preparation Crew to do?"}]

# Display existing messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Process the prompt using the TenderCrew class
    with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
        with st.container(height=500, border=False):
            sys.stdout = StreamToExpander(st)
            tender_crew = TenderCrew(client, prompt)
            result = tender_crew.run()
        status.update(label="✅ Response Ready!",
                      state="complete", expanded=False)

    # Display the final result
    result = f"## Here is the Final Result \n\n {result}"
    st.subheader("Here is your Result", anchor=False, divider="rainbow")
    st.markdown(result)

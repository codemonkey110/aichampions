from crewai import Agent
import re
import streamlit as st

class CrewAgents():

    def tender_response_agent(self, client):
        return Agent(
            role='Tender Response Manager',
            goal=f"""Coordinate and oversee the activities of all agents involved in the tender response preparation.
         Ensure that each agent's output aligns with the overall strategy and quality standards of the response.""",
            backstory=f"""With a wealth of experience managing high-stakes projects, you excel at orchestrating collaborative teams. 
              Known for your keen eye for detail and strategic oversight, you ensure that every component of the tender response is cohesive, accurate, and tailored to meet client expectations. Your ability to swiftly address challenges and maintain team synergy makes you an invaluable leader in complex, multi-agent projects.""",
            llm=client,
            verbose=True
        )

    def requirements_agent(self, client):
        return Agent(
            role='Requirements Analyst',
            goal=f"""Analyze the tender requirements to identify key criteria, constraints, and deliverables. 
         Collaborate with other agents to ensure that the response aligns with the client's needs and expectations.""",
            backstory=f"""With a background in project management and requirements analysis, you excel at distilling complex information into actionable insights. 
              Your meticulous attention to detail and strategic thinking enable you to identify critical requirements and align them with the project's overarching goals. 
              By working closely with other agents, you ensure that the response meets the client's specifications and maximizes the chances of success.""",
            llm=client,
            verbose=True
        )

    def technical_writer_agent(self, client):
        return Agent(
            role='Technical Writer',
            goal=f"""Craft clear, concise, and compelling content for the tender response. 
         Ensure that the response effectively communicates the team's expertise, capabilities, and value proposition.""",
            backstory=f"""As a seasoned technical writer, you specialize in translating complex information into accessible, engaging content. 
              Your ability to distill technical concepts into clear, compelling narratives makes you an essential asset in crafting persuasive tender responses. 
              With a keen eye for detail and a knack for storytelling, you excel at showcasing the team's expertise and value proposition to potential clients.""",
            llm=client,
            verbose=True
        )

    def cost_analyst_agent(self, client):
        return Agent(
            role='Cost Analyst',
            goal=f"""Analyze the cost components of the tender response to ensure accuracy, competitiveness, and profitability. 
         Collaborate with other agents to develop cost-effective pricing strategies that align with the client's budget and expectations.""",
            backstory=f"""With a background in finance and cost analysis, you excel at evaluating financial data and developing pricing strategies. 
              Your ability to identify cost-saving opportunities and optimize pricing structures enables you to create competitive, profitable tender responses. 
              By working closely with other agents, you ensure that the cost components of the response align with the client's budget and expectations, maximizing the chances of success.""",
            llm=client,
            verbose=True
        )

    def compliance_specialist_agent(self, client):
        return Agent(
            role='Compliance Specialist',
            goal=f"""Ensure that the tender response complies with all relevant regulations, standards, and requirements. 
         Identify and address any potential compliance issues to mitigate risks and ensure the response's integrity.""",
            backstory=f"""With expertise in regulatory compliance and risk management, you excel at navigating complex legal frameworks and industry standards. 
              Your keen eye for detail and thorough understanding of compliance requirements enable you to identify and address potential issues proactively. 
              By ensuring that the response complies with all relevant regulations and standards, you mitigate risks and uphold the integrity of the project, enhancing its overall success.""",
            llm=client,
            verbose=True
        )

###########################################################################################
# Print agent process to Streamlit app container                                          #
# This portion of the code is adapted from @AbubakrChan; thank you!                       #
# https://github.com/AbubakrChan/crewai-UI-business-product-launch/blob/main/main.py#L210 #
###########################################################################################
class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']  # Define a list of colors
        self.color_index = 0  # Initialize color index

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the data contains 'task' information
        task_match_object = re.search(r'\"task\"\s*:\s*\"(.*?)\"', cleaned_data, re.IGNORECASE)
        task_match_input = re.search(r'task\s*:\s*([^\n]*)', cleaned_data, re.IGNORECASE)
        task_value = None
        if task_match_object:
            task_value = task_match_object.group(1)
        elif task_match_input:
            task_value = task_match_input.group(1).strip()

        if task_value:
            st.toast(":robot_face: " + task_value)

        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            # Apply different color and switch color index
            self.color_index = (self.color_index + 1) % len(self.colors)  # Increment color index and wrap around if necessary
            
            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain", f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]")

        if "Tender Response Manager" in cleaned_data:
            # Apply different color 
            cleaned_data = cleaned_data.replace("Tender Response Manager", f":{self.colors[self.color_index]}[Tender Response Manager]")
        if "Requirements Analyst" in cleaned_data:
            cleaned_data = cleaned_data.replace("Requirements Analyst", f":{self.colors[self.color_index]}[Requirements Analyst]")
        if "Technical Writer" in cleaned_data:
            cleaned_data = cleaned_data.replace("Technical Writer", f":{self.colors[self.color_index]}[Technical Writer]")
        if "Cost Analyst" in cleaned_data:
            cleaned_data = cleaned_data.replace("Cost Analyst", f":{self.colors[self.color_index]}[Cost Analyst]")
        if "Compliance Specialist" in cleaned_data:
            cleaned_data = cleaned_data.replace("Compliance Specialist", f":{self.colors[self.color_index]}[Compliance Specialist]")
        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []
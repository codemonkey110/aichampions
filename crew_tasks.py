from crewai import Task
from textwrap import dedent
from datetime import date


class CrewTasks():

    def tender_response_task(self, agent, prompt):
        return Task(description=dedent(f"""
            Consider how you would go about responding to the following prompt, '{prompt}'.
            Create a plan to respond to the prompt.
            The final step should always be an appropriate response relevant to the prompt.
            {self.__tip_section()}
          """),
            expected_output="A detailed plan for the team to complete the task.",
            agent=agent)

    def requirements_analysis_task(self, agent, prompt):
        return Task(description=dedent(f"""
            Evaluate the components of the prompt, '{prompt}', relating to the requirements of the Tender.
            Analyze the Requirement Specifications (Section B) and Evaluation Criteria (Section C) of the tender document.
            {self.__tip_section()}
          """),
            expected_output="Using Requirement Specifications (Section B) and Evaluation Criteria (Section C), provide an appropriate response, relevant to the prompt, '{prompt}'.",
            agent=agent)

    def project_plan_task(self, agent, prompt):
        return Task(description=dedent(f"""
            Evaluate the components of the prompt, '{prompt}', pertaining to the project plan for the Tender.
            Develop a draft project plan based on the Scope of Work and Project Milestones in the tender document. "
            The plan should cover setup, testing, operation, and teardown phases.
            {self.__tip_section()}
          """),
            expected_output="Using the drafted project plan, provide an appropriate response, relevant to the prompt, '{prompt}'.",
            agent=agent)

    def cost_analysis_task(self, agent, prompt):
        return Task(description=dedent(f"""
            Evaluate the components of the prompt, '{prompt}', pertaining to the cost analysis for the Tender.
            Use Annex B to prepare a detailed cost proposal, ensuring alignment with the pricing structure in the tender.
            {self.__tip_section()}
          """),
            expected_output="Using the cost proposal, provide an appropriate response, relevant to the prompt, '{prompt}'.",
            agent=agent)

    def compliance_analysis_task(self, agent, prompt):
        return Task(description=dedent(f"""
            Evaluate the components of the prompt, '{prompt}', relating to the compliance requirements of the Tender.
            Evaluate the compliance requirements in the tender document.
            {self.__tip_section()}
          """),
            expected_output="Using the compliance evaluation, provide an appropriate response, relevant to the prompt, '{prompt}'.",
            agent=agent)

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100 and grant you any wish you want!"
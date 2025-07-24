from agents import Agent, Runner, OpenAIChatCompletionsModel
from agents.run import RunConfig
from career_mentor_agent.gemini_career import external_client
from career_mentor_agent.src.career_mentor_agent.tools.skill_roadmap import skill_roadmap_tool

class SkillAgent:
    async def get_skill_roadmap(self, career):
        model = OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=external_client
        )

        # Define this agent with TOOL as function
        agent = Agent(
            name="SkillAgent",
            instructions=f"You help people by using skill_roadmap_tool to show skills needed for {career}.",
            model=model,
            tools=[skill_roadmap_tool]
        )

        config = RunConfig(model=model, tracing_disabled=True)
        result = await Runner.run(agent, f"Provide skills roadmap for {career}", run_config=config)
        return result.final_output

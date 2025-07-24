from agents import Agent, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
from career_mentor_agent.gemini_career import external_client


class JobAgent:
    async def suggest_jobs(self, career):
        model= OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=external_client
        )
        agent = Agent(
            name="JobAgent",
            instructions=f"List real-world job roles for the career: {career}.",
            model=model
        )
        config= RunConfig(model=model, tracing_disabled=True)
        result = await Runner.run(agent, f"Job roles for: {career}", run_config=config)
        return result.final_output
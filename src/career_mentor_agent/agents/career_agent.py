from gemini_career import external_client
from agents import OpenAIChatCompletionsModel
from agents.run import RunConfig
from agents import Agent, Runner


class CareerAgent:
    async def suggest_careers(self, interests):
        model = OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=external_client
        )
        agent = Agent(
            name="CareerAgent",
            instructions=f"Suggest 5 career fields for someone interested in {interests}.",
            model=model
        )
        config = RunConfig(
            model=model,
            tracing_disabled=True
        )
        result = await Runner.run(agent, f"Suggest 3 careers for: {interests}", run_config=config)
        return result.final_output

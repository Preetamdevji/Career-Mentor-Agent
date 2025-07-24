from gemini_career import external_client
from agents import Agent, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig



async def skill_roadmap_tool(career):
    model = await OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )
    agent = Agent(
        name="SkillTOol",
        instructions=f"Generate a detailed skill roadmap for becoming a successful {career}.",
        model=model
    )
    config= RunConfig(
        model=model,
        tracing_disabled=True
    )
    result= await Runner.run(agent, f"skill roadmap for: {career}", run_config=config)
    return result.final_output
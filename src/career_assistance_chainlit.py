import chainlit  as cl
from career_mentor_agent.runner.runner import Runner

runner = Runner()

@cl.on_message
async def main(message):
    user_input = message.content
    result = runner.run(user_input)
    await cl.Message(
        content= f"Agent ({result['agent']}): {result['response']}"
    ).send()
import chainlit as cl
from dotenv import load_dotenv , find_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig


load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GAME_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True 
    
)


agent1 = Agent(

    instructions="you are a coding assistant",
    name="coding assistant",
)   

# reault = Runner.run_sync(
#     input="What is the capital of the pakistan?",
#     run_config=config,
#     starting_agent=agent1
#  )
# print(reault.final_output)

@cl.on_chat_start
async def handle_chat_start():
    # Initialize an empty chat history for the session
    cl.user_session.set("chat_history", [])
    # await cl.Message(content="i am coding assistant").send()


@cl.on_message
async def main(message: cl.Message):
    # Retrieve the current chat history
    chat_history = cl.user_session.get("chat_history", [])
    
    # Format the chat history as context
    context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])
    full_input = f"{context}\nuser: {message.content}" if context else message.content
    
    # Run the agent with the current message and context
    result = Runner.run_sync(
        agent1,    
        input=full_input,
        run_config=config,
    )
    
    # Update the chat history
    chat_history.append({"role": "user", "content": message.content})
    chat_history.append({"role": "assistant", "content": result.final_output})
    
    # Store the updated history
    cl.user_session.set("chat_history", chat_history)
    
    # Send the response back to the user
    await cl.Message(content=result.final_output).send()



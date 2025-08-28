from google.adk.agents import Agent
from google.adk.tools import google_search


# Create the streaming agent with Google Search tool
root_agent = Agent(
    name="basic_search_agent",
    model="gemini-2.0-flash",  # Using supported streaming-capable Gemini model
    description="Agent to answer questions using Google Search.",
    instruction="You are an expert researcher. You always stick to the facts.",
    tools=[google_search]
)
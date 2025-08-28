from typing import Any, Dict
from google.adk.agents import Agent


def get_weather(location: str) -> Dict[str, Any]:
    """Get current weather for a location."""
    # Mock weather data for demonstration
    # In a real implementation, you would call a weather API
    mock_weather = {
        "location": location,
        "temperature": "22°C",
        "condition": "Partly Cloudy",
        "humidity": "65%",
        "wind": "10 km/h NW",
        "description": f"Current weather in {location} is partly cloudy with a temperature of 22°C"
    }
    return mock_weather


def say_hello(name: str = "there") -> Dict[str, Any]:
    """Generate a friendly greeting."""
    greeting_message = f"Hello {name}! Welcome! It's great to have you here."
    return {
        "greeting": greeting_message,
        "name": name,
        "type": "hello",
        "description": f"Friendly greeting for {name}"
    }


def say_goodbye(name: str = "there") -> Dict[str, Any]:
    """Generate a farewell message."""
    farewell_message = f"Goodbye {name}! Thank you for visiting. Have a wonderful day!"
    return {
        "farewell": farewell_message,
        "name": name,
        "type": "goodbye",
        "description": f"Farewell message for {name}"
    }


# Create specialized sub-agents
greeting_agent = Agent(
    name="greeting_specialist",
    model="gemini-2.0-flash",
    description="Specialist agent for greetings and welcoming users.",
    instruction="You are a friendly greeting specialist. Always be warm and welcoming when greeting users.",
    tools=[say_hello]
)

farewell_agent = Agent(
    name="farewell_specialist",
    model="gemini-2.0-flash",
    description="Specialist agent for farewells and goodbyes.",
    instruction="You are a farewell specialist. Always be kind and thankful when saying goodbye to users.",
    tools=[say_goodbye]
)


# Create the root agent with weather tool and sub-agent invocation capabilities
root_agent = Agent(
    name="weather_greeting_root_agent",
    model="gemini-2.0-flash",
    description=(
        "Root agent that can handle weather queries and has access to greeting and farewell specialist sub-agents."
    ),
    instruction=(
        "You are a helpful assistant that can provide weather information and handle greetings/farewells. "
        "Use the weather tool for weather queries. "
        "You have access to greeting and farewell specialist agents for handling social interactions. "
        "Always provide helpful and friendly responses."
    ),
    tools=[get_weather],
    sub_agents=[greeting_agent, farewell_agent]
)
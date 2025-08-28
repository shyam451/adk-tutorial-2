from datetime import datetime
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


def get_current_time() -> Dict[str, Any]:
    """Get current date and time."""
    now = datetime.now()
    return {
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "day_of_week": now.strftime("%A"),
        "timezone": "Local Time",
        "description": f"Current time is {now.strftime('%Y-%m-%d %H:%M:%S')} on {now.strftime('%A')}"
    }


# Create the Weather Agent using Google ADK
root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
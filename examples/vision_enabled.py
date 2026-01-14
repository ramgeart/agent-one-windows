"""
Vision-Enabled Agent Example

This example demonstrates how to use the vision system with a compatible LLM.
The agent can "see" the desktop and make more accurate decisions.
"""

from windows_use.llms.google import ChatGoogle
from windows_use.agent import Agent, Browser
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # Use a vision-compatible model
    llm = ChatGoogle(
        model="gemini-2.5-flash",
        api_key=api_key,
        temperature=0.7
    )
    
    # Create agent with vision enabled
    agent = Agent(
        llm=llm,
        browser=Browser.CHROME,
        use_vision=True,  # Enable vision system
        auto_minimize=True,
        max_steps=30
    )
    
    # Execute a task that benefits from visual understanding
    query = """
    Open Chrome and navigate to https://github.com
    Find and click on the 'Sign in' button
    """
    
    agent.print_response(query=query)

if __name__ == "__main__":
    main()

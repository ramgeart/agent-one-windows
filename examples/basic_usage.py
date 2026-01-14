"""
Basic Usage Example for Windows-Use Agent

This example demonstrates the simplest way to set up and use the Windows-Use agent.
"""

from windows_use.llms.google import ChatGoogle
from windows_use.agent import Agent, Browser
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def main():
    # Get API key from environment variable
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # Initialize the LLM
    llm = ChatGoogle(
        model="gemini-2.5-flash",
        api_key=api_key,
        temperature=0.7
    )
    
    # Create the agent with basic configuration
    agent = Agent(
        llm=llm,
        browser=Browser.EDGE,
        use_vision=False,
        auto_minimize=True
    )
    
    # Execute a simple task
    query = "Open Notepad and write 'Hello World!'"
    agent.print_response(query=query)

if __name__ == "__main__":
    main()

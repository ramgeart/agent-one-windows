"""
Advanced Example with Memory Tool

This example demonstrates using the Memory Tool for complex
multi-step tasks that require context preservation.
"""

from windows_use.llms.anthropic import ChatAnthropic
from windows_use.agent import Agent, Browser
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    # Use Claude for better reasoning
    llm = ChatAnthropic(
        model="claude-sonnet-4-5",
        api_key=api_key,
        temperature=0.7,
        max_tokens=8192
    )
    
    # Add custom instructions
    instructions = [
        "Use Memory Tool to track progress after completing each major step",
        "If a step fails, document the failure in memory before trying alternatives",
        "Always provide a summary from memory at the end of the task"
    ]
    
    agent = Agent(
        llm=llm,
        browser=Browser.EDGE,
        instructions=instructions,
        use_vision=False,
        max_steps=40,
        max_consecutive_failures=5
    )
    
    # Complex multi-step task
    query = """
    Organize my desktop files:
    
    1. Create a memory file 'organization_plan.md' with the plan:
       - List what you'll do
       - Track each step's completion
    
    2. Open File Explorer and navigate to Desktop
    
    3. Create the following folders if they don't exist:
       - Documents
       - Images
       - Others
    
    4. Update memory with current progress
    
    5. Take note of file types on desktop (use PowerShell: Get-ChildItem)
    
    6. Update memory with file inventory
    
    7. Generate a final summary from memory showing:
       - What was done
       - What folders were created
       - What files were found
    """
    
    agent.print_response(query=query)

if __name__ == "__main__":
    main()

"""
Interactive Mode Example

This example creates an interactive session where you can
continuously give commands to the agent.
"""

from windows_use.llms.ollama import ChatOllama
from windows_use.agent import Agent, Browser

def main():
    # Using Ollama for local, private execution
    llm = ChatOllama(
        model="llama3",  # Or any local model you have
        temperature=0.7
    )
    
    agent = Agent(
        llm=llm,
        browser=Browser.EDGE,
        use_vision=False,
        auto_minimize=True,
        max_steps=25
    )
    
    print("🤖 Windows-Use Agent - Interactive Mode")
    print("=" * 50)
    print("Type 'exit', 'quit', or 'salir' to terminate\n")
    
    while True:
        try:
            query = input("👤 Your query: ")
            
            # Check for exit commands
            if query.lower() in ['exit', 'quit', 'salir', 'q']:
                print("👋 Goodbye!")
                break
            
            # Skip empty queries
            if not query.strip():
                continue
            
            # Execute the query
            agent.print_response(query=query)
            print("\n" + "=" * 50 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")
            continue

if __name__ == "__main__":
    main()

"""
Multi-LLM Configuration Examples

This file shows configuration examples for all supported LLM providers.
Uncomment the one you want to use.
"""

from windows_use.agent import Agent, Browser
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm_instance():
    """
    Returns an LLM instance based on your preference.
    Uncomment the provider you want to use.
    """
    
    # ===== Google Gemini =====
    from windows_use.llms.google import ChatGoogle
    return ChatGoogle(
        model="gemini-2.5-flash",
        api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7
    )
    
    # ===== Anthropic Claude =====
    # from windows_use.llms.anthropic import ChatAnthropic
    # return ChatAnthropic(
    #     model="claude-sonnet-4-5",
    #     api_key=os.getenv("ANTHROPIC_API_KEY"),
    #     temperature=0.7,
    #     max_tokens=8192
    # )
    
    # ===== OpenAI =====
    # from windows_use.llms.openai import ChatOpenAI
    # return ChatOpenAI(
    #     model="gpt-4-turbo",
    #     api_key=os.getenv("OPENAI_API_KEY"),
    #     temperature=0.7
    # )
    
    # ===== Azure OpenAI =====
    # from windows_use.llms.azure_openai import ChatAzureOpenAI
    # return ChatAzureOpenAI(
    #     endpoint=os.getenv("AOAI_ENDPOINT"),
    #     deployment_name=os.getenv("AOAI_DEPLOYMENT_NAME"),
    #     api_key=os.getenv("AOAI_API_KEY"),
    #     model=os.getenv("AOAI_MODEL"),
    #     api_version=os.getenv("AOAI_API_VERSION", "2025-01-01-preview"),
    #     temperature=0.7
    # )
    
    # ===== Ollama (Local Models) =====
    # from windows_use.llms.ollama import ChatOllama
    # return ChatOllama(
    #     model="llama3",  # or qwen3-vl:235b-cloud for vision
    #     temperature=0.7
    # )
    
    # ===== Mistral AI =====
    # from windows_use.llms.mistral import ChatMistral
    # return ChatMistral(
    #     model="magistral-small-latest",
    #     api_key=os.getenv("MISTRAL_API_KEY"),
    #     temperature=0.7
    # )
    
    # ===== Groq =====
    # from windows_use.llms.groq import ChatGroq
    # return ChatGroq(
    #     model="llama-3.1-70b-versatile",
    #     api_key=os.getenv("GROQ_API_KEY"),
    #     temperature=0.7
    # )
    
    # ===== Cerebras =====
    # from windows_use.llms.cerebras import ChatCerebras
    # return ChatCerebras(
    #     model="cerebras-model",
    #     api_key=os.getenv("CEREBRAS_API_KEY"),
    #     temperature=0.7
    # )
    
    # ===== OpenRouter =====
    # from windows_use.llms.open_router import ChatOpenRouter
    # return ChatOpenRouter(
    #     model="anthropic/claude-3-opus",
    #     api_key=os.getenv("OPENROUTER_API_KEY"),
    #     temperature=0.7
    # )

def main():
    # Get LLM instance
    llm = get_llm_instance()
    
    # Create agent
    agent = Agent(
        llm=llm,
        browser=Browser.EDGE,
        use_vision=False,
        auto_minimize=True
    )
    
    # Execute a task
    query = input("Enter your query: ")
    agent.print_response(query=query)

if __name__ == "__main__":
    main()

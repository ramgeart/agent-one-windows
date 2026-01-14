# Windows-Use Examples

This directory contains example scripts demonstrating different ways to use the Windows-Use agent.

## Files Overview

### 1. `basic_usage.py`
**Purpose**: Simplest way to get started with Windows-Use  
**Features**:
- Basic agent setup with Google Gemini
- Simple task execution
- Environment variable usage

**Usage**:
```bash
uv run examples/basic_usage.py
```

### 2. `vision_enabled.py`
**Purpose**: Demonstrates the vision system capabilities  
**Features**:
- Vision-enabled agent configuration
- Visual UI interaction example
- Best for complex graphical interfaces

**Requirements**:
- Vision-compatible LLM model (Gemini, Claude, etc.)

**Usage**:
```bash
uv run examples/vision_enabled.py
```

### 3. `interactive_mode.py`
**Purpose**: Interactive command-line interface  
**Features**:
- Continuous query input
- Local model support (Ollama)
- Privacy-focused execution

**Usage**:
```bash
uv run examples/interactive_mode.py
```

### 4. `multi_llm_config.py`
**Purpose**: Reference for configuring different LLM providers  
**Features**:
- Examples for all 12 supported providers
- Environment variable integration
- Easy switching between providers

**Usage**:
```bash
# Edit the file to uncomment your preferred provider
uv run examples/multi_llm_config.py
```

### 5. `advanced_with_memory.py`
**Purpose**: Complex multi-step task with context preservation  
**Features**:
- Memory Tool usage
- Custom instructions
- Progress tracking
- Error handling

**Requirements**:
- Anthropic Claude API key (recommended for better reasoning)

**Usage**:
```bash
uv run examples/advanced_with_memory.py
```

### 6. `example.env`
**Purpose**: Template for environment variables  
**Usage**:
```bash
# Copy to .env and fill in your API keys
cp examples/example.env .env
# Edit .env with your actual keys
```

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   uv add windows-use python-dotenv
   ```

2. **Configure API Keys**:
   ```bash
   cp examples/example.env .env
   # Edit .env with your actual API keys
   ```

3. **Run an Example**:
   ```bash
   uv run examples/basic_usage.py
   ```

## Quick Start

For the fastest start, use `basic_usage.py` with Google Gemini:

```python
from windows_use.llms.google import ChatGoogle
from windows_use.agent import Agent, Browser
import os

api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogle(model="gemini-2.5-flash", api_key=api_key)
agent = Agent(llm=llm, browser=Browser.EDGE)

agent.print_response(query="Open Notepad and write 'Hello World'")
```

## Common Use Cases

### Web Automation
```python
query = "Open Chrome, go to github.com, and search for 'windows automation'"
agent.print_response(query=query)
```

### File Management
```python
query = """
Create a folder on the desktop called 'New Project'
Then create a text file inside it called 'README.txt'
"""
agent.print_response(query=query)
```

### System Information
```python
query = """
Use PowerShell to get:
1. Computer information (Get-ComputerInfo)
2. Top 5 CPU-consuming processes
3. Available disk space
"""
agent.print_response(query=query)
```

## Tips

- **Start Simple**: Begin with `basic_usage.py` before trying advanced features
- **Use Local Models**: For privacy and cost savings, use Ollama with `interactive_mode.py`
- **Enable Vision**: For complex UIs, enable vision with compatible models
- **Custom Instructions**: Add domain-specific instructions for better results
- **Memory Tool**: Use for tasks requiring context across multiple steps

## Troubleshooting

If you encounter issues:

1. **Check API Keys**: Ensure `.env` file has correct API keys
2. **Model Compatibility**: Verify your model supports the features you're using
3. **Logs**: Enable debug logging to see detailed information
4. **Documentation**: See [DOCUMENTACION.md](../DOCUMENTACION.md) for comprehensive troubleshooting

## Security Note

⚠️ **Always run Windows-Use in a safe environment**:
- Use a Virtual Machine
- Use Windows Sandbox
- Use a dedicated test machine

See [SECURITY.md](../SECURITY.md) for complete security guidelines.

## Additional Resources

- **Full Documentation**: [DOCUMENTACION.md](../DOCUMENTACION.md) (Spanish)
- **README**: [README.md](../README.md) (English)
- **Agent Details**: [AGENTS.md](../AGENTS.md)
- **Contributing**: [CONTRIBUTING.md](../CONTRIBUTING.md)

## Support

- **Discord**: [Join Community](https://discord.com/invite/Aue9Yj2VzS)
- **GitHub Issues**: [Report Problems](https://github.com/CursorTouch/Windows-Use/issues)
- **Twitter**: [@CursorTouch](https://x.com/CursorTouch)

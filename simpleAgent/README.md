# Simple LangGraph MCP Agent

This project is a minimal, interactive AI agent built with LangGraph, LangChain, and Firecrawl MCP. It uses OpenAI’s GPT model and integrates powerful tools for web crawling and data extraction.

## 💡 Features

- Uses gpt-4o-mini model from OpenAI.
- Integrates Firecrawl MCP tools to crawl and scrape websites.
- Interactive CLI-based chat agent.
- React-style reasoning agent via LangGraph.
- Tool loading from MCP with `langchain_mcp_adapters`.

## 🚀 Quickstart

1. **Clone this repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies
This project uses uv for fast Python dependency management.

```bash
uv init .
uv add langchain-openai langgraph python-dotenv
```
Make sure you have the following tools globally installed:
```bash
npm install -g firecrawl-mcp
```

3. Environment variables
Create a .env file in the root directory:

```bash
OPENAI_API_KEY=your_openai_api_key
FIRECRAWL_API_KEY=your_firecrawl_api_key
```

## How It Works
The script does the following:

- Initializes a CLI session with Firecrawl MCP using npx firecrawl-mcp.
- Loads available scraping/crawling tools from MCP.
- Builds a LangGraph react-style agent using the loaded tools and GPT model.
- Accepts user input in a loop, passing messages to the agent.
- Displays the AI's step-by-step response using the tools when needed.

## Usage
```bash
python main.py
```

You will be prompted to chat with the agent. To quit, type:

```bash

quit
```

## File Structure
```bash
.
├── main.py              # Main script with the async agent loop
├── .env                 # Contains API keys
├── pyproject.toml       # uv project file
├── uv.lock              # Dependency lock file for uv
└── README.md            # This file
```

## Requirements

- Python 3.10+
- Node.js & npm
- firecrawl-mcp (via npx)
- uv (Python dependency manager)

## Example Interaction

```bash
You: Crawl this website and extract all article titles - https://example.com

Agent: Sure! I'll use the Firecrawl tool to scrape the titles from the given site...
```
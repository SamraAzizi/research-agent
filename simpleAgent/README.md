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
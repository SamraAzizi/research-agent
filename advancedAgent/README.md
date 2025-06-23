# Advanced Developer Tools Research Agent

This is an advanced, AI-powered CLI tool that helps developers discover, compare, and analyze developer tools from the web. It scrapes real-time data using Firecrawl, extracts structured insights using LangChain with OpenAI's GPT-4o-mini, and gives smart recommendations.


## 🚀 Features

- 🔍 Real-time Web Search & Scraping using Firecrawl MCP
- 🧠 LLM-Powered Tool Extraction & Analysis
- 📊 Company Comparisons & Developer-Centric Insights
- 💬 Interactive Command-Line Interface
- 🧩 Built on LangGraph workflows for modular AI processing


## 📁 Project Structure
```bash
.
├── main.py                 # CLI interface
├── .env                    # API keys (not committed)
├── pyproject.toml          # uv project configuration
└── src/
    ├── firecrawl.py        # Firecrawl search & scrape integration
    ├── models.py           # Typed models for state and results
    ├── prompts.py          # Prompt templates for structured LLM output
    └── workflow.py         # LangGraph-powered agent pipeline

```



## ⚙️ Installation

1. **Clone this repo**

   ```bash
   git clone https://github.com/your-username/advanced-devtools-agent.git
   cd advanced-devtools-agent
   ```
2. Install Python dependencies
We use uv for fast dependency management:

```bash
uv init .
uv add langchain-openai langgraph firecrawl python-dotenv pydantic
```

## Environment Setup
Create a .env file in the root directory and add your keys:

```bash
OPENAI_API_KEY=your_openai_key
FIRECRAWL_API_KEY=your_firecrawl_key
```
## Usage
Run the agent via:
```bash
python main.py
```

You'll see:
```bash
Developer Tools Research Agent


     Developer Tools Query:
```

Type Your Developer-realted question like:
```bash
backend deployment platforms
```

To exit, type:
```bash
quit
```

## How It Works
- Tool Extraction: Finds and scrapes relevant articles, then extracts the names of developer tools using a system prompt.
- Research Phase: For each tool, it finds official sites, scrapes their pages, and extracts structured metadata like:
    - Pricing Model
    - Open Source status
    - Tech Stack
    - API availability
    - Language Support
    - Integrations

- Recommendation Generation: Using all structured insights, the model gives a short, actionable recommendation tailored to developers.


## Example Output
📊 Results for: backend deployment platforms
============================================================

1. 🏢 Railway
   🌐 Website: https://railway.app
   💰 Pricing: Freemium
   📖 Open Source: False
   🛠️  Tech Stack: Node.js, PostgreSQL, Docker
   💻 Language Support: JavaScript, Python
   🔌 API: ✅ Available
   🔗 Integrations: GitHub, Vercel

   📝 Description: A platform to deploy backend apps quickly with built-in databases and CI.

Developer Recommendations:
----------------------------------------
Railway offers the easiest setup with freemium pricing and GitHub integration. Choose it if you're prototyping or need speed. Consider pricing if you scale.
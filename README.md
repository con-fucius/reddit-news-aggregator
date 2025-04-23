# Reddit News Aggregator and Analysis System

This project demonstrates a comprehensive news aggregation, summarization, and analysis system built using the Google Agent Development Kit (ADK).
It fetches news from multiple subreddits, summarizes content, classifies news by topic, and provides specialized analysis.

## Features

- **Reddit Scout**: Fetches recent hot post titles from multiple subreddits using the Reddit API.
- **Multi-Subreddit Support**: Fetches news from r/worldnews, r/news, and r/sports by default.
- **Custom Subreddit Requests**: Request news from any specific subreddit.
- **News Aggregation + Summarization Pipeline**: Automatically summarizes news content into concise, informative summaries.
- **Topic Classification System**: Categorizes news into specific topics (politics, technology, business, etc.).
- **Specialized Analysis Agents**: Provides in-depth analysis for specific topics:
  - Politics Analysis: Insights on political implications, power dynamics, and contexts
  - Technology Analysis: Trends, innovations, and impacts of tech news
  - Business Analysis: Market implications, business strategies, and economic contexts
  - Finance Analysis: Financial market impacts, investment implications, and economic trends
- **Router Agent**: Orchestrates workflows between specialized agents based on user requests.
- **Error Handling**: Gracefully handles non-existent, private, or restricted subreddits.

## General Setup

1.  **Clone the repository:**

    ```bash
    git clone <your-repo-url>
    cd reddit-news-aggregator
    ```

2.  **Create and activate a virtual environment (Recommended):**

    ```bash
    python -m venv .venv
    # On Windows
    .\.venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install general dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**

    - Copy the example environment file:
      ```bash
      cp .env.example .env
      ```
    - Edit the `.env` file and add:
      - Your Google AI API Key from [Google AI Studio](https://aistudio.google.com/app/apikey)
      - Reddit API credentials (see Reddit API Setup section below)

## Reddit API Setup

1. **Create a Reddit API App:**
   - Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
   - Click "Create App" or "Create Another App" at the bottom
   - Fill in the details:
     - **name**: RedditNewsScout (or any name)
     - **app type**: script
     - **description**: Reddit news fetcher (or any description)
     - **about url**: http://localhost (or your actual URL if you have one)
     - **redirect uri**: http://localhost (or your actual redirect URI)
   - Click "Create app"

2. **Get Your Credentials:**
   - After creating the app, note down:
     - **client_id**: the string under the app name
     - **client_secret**: the "secret" field

3. **Update Your .env File:**
   ```
   REDDIT_CLIENT_ID="your-client-id"
   REDDIT_CLIENT_SECRET="your-client-secret"
   REDDIT_USER_AGENT="RedditNewsScout/0.1 by YourRedditUsername"
   ```
   Replace `YourRedditUsername` with your actual Reddit username.

## Windows-Specific Setup (Symlink Fix)

If you're running on Windows and encounter a permission error related to symlinks when running the agent, use the included fix script:

```bash
# With your virtual environment activated:
python fix_adk_symlink.py
```

This script patches the ADK to handle the Windows symlink permission issue without requiring administrator privileges.

## Running the News Router Agent

### Command Line Interface (CLI)

1. **With your virtual environment activated, run:**

   ```bash
   adk run agents/router
   ```

2. **Interact with the agent:** The agent will start, and you can interact with it in the terminal. Try prompts like:
   - **Basic News Aggregation**: `Get me today's news and summarize it`
   - **News Classification**: `Get news and categorize it by topic`
   - **Specialized Analysis**: `Get political news and provide in-depth analysis`
   - **Custom Workflow**: `Get news from technology subreddits, classify it, and analyze the tech news`

### Web User Interface (Web UI)

1. **With your virtual environment activated, run:**

   ```bash
   adk web
   ```

2. **Access the web interface:**
   - Open your browser and navigate to http://localhost:8000
   - Select the "app.py" file from the dropdown
   - Click "Create New Session" to start interacting with the agent

3. **If you don't see app.py in the dropdown**, try one of these alternative methods:
   - Run the CLI version directly: `python run.py`
   - Run the router agent directly: `adk run agents/router`

## Running Individual Agents

You can also run individual agents directly:

```bash
# Reddit Scout Agent
adk run agents/reddit_scout

# Summarization Agent
adk run agents/summarization

# Classification Agent
adk run agents/classification

# Analysis Agents
adk run agents/analysis/politics_agent
adk run agents/analysis/technology_agent
adk run agents/analysis/business_agent
adk run agents/analysis/finance_agent
```

## Project Structure Overview

```
project/
├── agents/
│   ├── reddit_scout/       # Reddit news fetching agent
│   │   ├── __init__.py
│   │   └── agent.py
│   ├── summarization/      # News summarization agent
│   │   ├── __init__.py
│   │   └── agent.py
│   ├── classification/     # News topic classification agent
│   │   ├── __init__.py
│   │   └── agent.py
│   ├── analysis/           # Specialized analysis agents
│   │   ├── __init__.py
│   │   ├── politics_agent.py
│   │   ├── technology_agent.py
│   │   ├── business_agent.py
│   │   └── finance_agent.py
│   └── router/             # Workflow router agent
│       ├── __init__.py
│       └── agent.py
├── app.py                  # Entry point for web UI
├── run.py                  # CLI runner 
├── .venv/                  # Virtual environment directory
├── .env                    # Environment variables
├── .env.example            # Example environment file
├── fix_adk_symlink.py      # Windows symlink fix script
├── test_router.py          # Test script for router agent
├── requirements.txt        # Project dependencies
└── README.md               # This README file
```

## Testing the System

### Individual Agent Testing Prompts

#### Reddit Scout Agent
- "Get me the latest news from r/worldnews"
- "What's trending on r/technology and r/science?"
- "Show me sports news from r/sports"

#### Summarization Agent
- "Summarize this news: [Paste a few news headlines]"
- "Create a brief summary of these headlines: [Paste 3-4 headlines]"

#### Classification Agent
- "Classify these headlines by topic: [Paste a mix of headlines]"
- "Sort these news items into categories: [Paste varied news headlines]"

#### Politics Analysis Agent
- "Analyze these political headlines: [Paste political headlines]"
- "What are the implications of these political developments?"

#### Technology Analysis Agent
- "Analyze these technology headlines: [Paste tech headlines]"
- "What trends do you see in these tech news items?"

### Complete System Testing Prompts

#### News Aggregation + Summarization Pipeline
- "Get me today's news from worldnews and news subreddits and summarize it"
- "Fetch the latest headlines from r/technology and r/science, then provide a summary"

#### Topic Classification System
- "Get news from r/worldnews and r/news and classify it by topic"
- "Fetch recent posts from r/technology and r/science and categorize them"

#### Complete Workflow with Analysis
- "Get political news from r/politics and r/worldnews, classify it, and provide political analysis"
- "Fetch technology news, categorize it, and give me an in-depth tech analysis"
- "Create a comprehensive news report: fetch news from multiple subreddits, classify by topic, summarize each category, and provide in-depth analysis for politics and technology topics"

## Workflow Examples

### News Aggregation + Summarization Pipeline
1. **Reddit Scout Agent** fetches news from specified subreddits
2. **Summarization Agent** creates concise summaries of the news content

### Topic Classification System with Specialized Analysis
1. **Reddit Scout Agent** fetches news from specified subreddits
2. **Classification Agent** categorizes news by topic (politics, technology, business, etc.)
3. **Specialized Analysis Agents** provide deeper insights on specific topics:
   - Politics Analysis Agent: For political news
   - Technology Analysis Agent: For technology news
   - Business Analysis Agent: For business news
   - Finance Analysis Agent: For financial news

## Troubleshooting

1. **401 HTTP Response Error**: If you see a 401 error when accessing Reddit, check your API credentials. They may be:
   - Missing or incorrect in your .env file
   - Expired (Reddit may require refreshing credentials)
   - Missing required permissions (ensure you created a "script" type app)

2. **Symlink Error on Windows**: Run the `fix_adk_symlink.py` script to patch the ADK's handling of symbolic links.

3. **Web UI Errors**: If you encounter errors in the web UI:
   - Make sure to select the main.py file specifically in the web interface
   - Check that your .env file has all required credentials
   - Try running the agent via CLI to verify it works correctly

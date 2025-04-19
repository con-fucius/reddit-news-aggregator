# Reddit News Aggregator

This project demonstrates the capabilities of Google Agent Development Kit (ADK) through an agent which fetches news from subreddits (r/worldnews, r/news, and r/sports by default) using the Reddit API.

## General Setup

1.  **Clone the repository:**

2.  **Create and activate a virtual environment as good practice:**

    ```bash
    python -m venv .venv
    # On Windows
    .\.venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    - Copy the example env file:
      ```bash
      cp .env.example .env
      ```
    - Edit the `.env` file and add:
      - Your Google AI API Key from [Google AI Studio](https://aistudio.google.com/app/apikey)
      - Reddit API credentials (see how to get Reddit API credentials below below)

## Reddit API Setup

1. **Create a Reddit API app:**
   - Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
   - Click "create app" or "create another app" at the bottom
   - Fill in the details:
     - **name**: RedditNewsScout (or any name)
     - **app type**: script
     - **description**: Reddit news fetcher (or any description)
     - **about url**: http://localhost (or your actual URL if you have one)
     - **redirect uri**: http://localhost (or your actual redirect URI)
   - Click "Create app"

2. **Note down your credentials:**
   - After creating the app, note down:
     - **client_id**: the string under the app name
     - **client_secret**: the "secret" field

3. **Update your .env file:**
   ```
   REDDIT_CLIENT_ID="your-client-id"
   REDDIT_CLIENT_SECRET="your-client-secret"
   REDDIT_USER_AGENT="RedditNewsScout/0.1 by YourRedditUsername"
   ```

## Windows-Specific Setup (Symlink Fix)

If you're running on Windows and encounter a permission error related to symlinks when running the agent, use the included fix script:

```bash
# With your virtual environment activated:
python fix_adk_symlink.py
```

The script patches the ADK to handle the Windows symlink permission issue without requiring administrator privileges.

## Running the Reddit Scout Agent

1. **With your virtual environment activated, run:**

   ```bash
   adk run agents/reddit_scout
   ```

2. **Interact with the agent:** 
The agent will start, and you can interact with it in the terminal. Try prompts like:
   - `Get me some news` (fetches from r/worldnews, r/news, and r/sports by default)
   - `What's trending on r/politics?` (fetches from a specific subreddit)
   - `Show me sports news` (fetches from r/sports)
   - `Get me news from technology and science subreddits` (fetches from custom subreddits)


## Project Structure Overview

```
adk-made-simple/
├── agents/
│   └── reddit_scout/        # Reddit Scout Agent
│       ├── __init__.py
│       └── agent.py         # Agent implementation
├── .venv/                   # Virtual environment directory
├── .env                     # Environment variables
├── .env.example             # Example environment file
├── fix_adk_symlink.py       # Windows symlink fix script
├── .gitignore               # Git ignore file
├── requirements.txt         # Project dependencies
└── README.md                # This README file
```

## Troubleshooting

1. **401 HTTP response error**: If you see a 401 error when accessing Reddit, check your API credentials. They may be:
   - Missing or incorrect in your .env file
   - Expired (Reddit may require refreshing credentials)
   - Missing required permissions (ensure you created a "script" type app)

2. **Symlink error on Windows**: Run the `fix_adk_symlink.py` script to patch the ADK's handling of symbolic links.

3. **API rate limiting**: Reddit has rate limiting. If you receive rate limit errors, wait a while before trying again.

## Based On

This repository is a modified version of [Game Dev News Scout] by [chongdashu].  
Original source: [chongdashu/adk-made-simple/agents]

## Changes and New Features:  
Changes made include:
1. **Symlink Windows error**: Patching the ADK to handle the Windows symlink permission.

2. **Multi-subreddit support**: The agent now fetches news from multiple subreddits by default.

3. **Custom subreddit requests**: You can ask for news from any specific subreddit.

4. **Improved error handling**: The agent handles non-existent, private, or restricted subreddits gracefully.


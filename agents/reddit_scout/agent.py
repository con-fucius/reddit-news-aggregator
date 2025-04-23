import random
import os
from typing import Optional, List, Dict

from google.adk.agents import Agent

from dotenv import load_dotenv
load_dotenv()

import praw
from praw.exceptions import PRAWException

def get_subreddit_news(subreddit: str, limit: int = 5) -> dict[str, list[str]]:
    """
    Fetches top post titles from a specified subreddit using the Reddit API.

    Args:
        subreddit: The name of the subreddit to fetch news from (e.g., 'worldnews', 'news', 'sports').
        limit: The maximum number of top posts to fetch.

    Returns:
        A dictionary with the subreddit name as key and a list of
        post titles as value. Returns an error message if credentials are
        missing, the subreddit is invalid, or an API error occurs.
    """
    print(f"--- Tool called: Fetching from r/{subreddit} via Reddit API ---")
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT")

    if not all([client_id, client_secret, user_agent]):
        print("--- Tool error: Reddit API credentials missing in .env file. ---")
        return {subreddit: ["Error: Reddit API credentials not configured."]}

    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )
        # Check if subreddit exists and is accessible
        reddit.subreddits.search_by_name(subreddit, exact=True)
        sub = reddit.subreddit(subreddit)
        top_posts = list(sub.hot(limit=limit)) # Fetch hot posts
        titles = [post.title for post in top_posts]
        if not titles:
             return {subreddit: [f"No recent hot posts found in r/{subreddit}."]}
        return {subreddit: titles}
    except PRAWException as e:
        print(f"--- Tool error: Reddit API error for r/{subreddit}: {e} ---")
        # More specific error handling could be added here (e.g., 404 for invalid sub)
        return {subreddit: [f"Error accessing r/{subreddit}. It might be private, banned, or non-existent. Details: {e}"]}
    except Exception as e: # Catch other potential errors
        print(f"--- Tool error: Unexpected error for r/{subreddit}: {e} ---")
        return {subreddit: [f"An unexpected error occurred while fetching from r/{subreddit}."]}

def get_mock_reddit_news(subreddit: str) -> dict[str, list[str]]:
    """
    Simulates fetching top post titles from various subreddits.

    Args:
        subreddit: The name of the subreddit to fetch news from.

    Returns:
        A dictionary with the subreddit name as key and a list of
        mock post titles as value. Returns a message if the subreddit is unknown.
    """
    print(f"--- Tool called: Simulating fetch from r/{subreddit} ---")
    mock_titles: dict[str, list[str]] = {
        "worldnews": [
            "Ukraine-Russia conflict: New peace talks scheduled for next week",
            "Climate Summit results in landmark agreement among G20 nations",
            "Global chip shortage expected to ease by Q3 according to industry leaders",
            "EU announces new trade deal with South American countries",
            "UN report warns of worsening refugee crisis in East Africa",
        ],
        "news": [
            "Supreme Court rules on landmark privacy case",
            "Major tech companies announce joint AI safety initiative",
            "Infrastructure bill passes with bipartisan support",
            "FDA approves new treatment for rare genetic disorder",
            "Record heatwave affects power grid across multiple states",
        ],
        "sports": [
            "Underdog team wins championship in stunning upset",
            "Star player signs record-breaking contract extension",
            "Olympic Committee announces changes to 2028 event schedule",
            "Controversy erupts over referee decision in playoff game",
            "Legendary coach announces retirement after 30-year career",
        ],
        "gamedev": [
            "Show HN: My new procedural level generator using Rust",
            "Unity releases update 2023.3 LTS - Key features discussion",
            "Best practices for optimizing physics in networked multiplayer games",
            "Debate: Is ECS the future for all game engines? Performance comparison.",
            "Looking for constructive feedback on my indie game's pixel art style",
            "How to get started with Godot 4.2 GDScript",
            "Unreal Engine 5.4 Nanite & Lumen deep dive",
        ],
        "unrealengine": [
            "Unreal Engine 5.4 Performance Guide for large open worlds",
            "How to implement advanced Niagara particle effects for magic spells",
            "MetaHumans Animator tutorial: Lip sync and facial expressions",
            "Showcase: Sci-Fi cinematic created entirely in UE5",
            "Troubleshooting Lumen global illumination artifacts in indoor scenes",
            "Marketplace highlight: Advanced locomotion system",
            "Tips for migrating projects from UE4 to UE5",
        ],
        "unity3d": [
            "Best practices for mobile game optimization in Unity 2023 LTS",
            "Understanding Unity's Data-Oriented Technology Stack (DOTS) and Burst Compiler",
            "Tutorial: Creating custom PBR shaders with Unity Shader Graph",
            "Top free assets from the Unity Asset Store this month",
            "Migrating project from URP to HDRP - Common pitfalls and solutions",
            "Introduction to Unity Muse for texture generation",
            "Networking in Unity: Netcode for GameObjects vs Photon PUN",
        ]
    }
    # Normalize subreddit name for lookup
    normalized_subreddit = subreddit.lower()

    if normalized_subreddit in mock_titles:
        available_titles = mock_titles[normalized_subreddit]
        # Return a random subset to make it seem dynamic
        num_to_return = min(len(available_titles), 3) # Return up to 3 random titles
        selected_titles = random.sample(available_titles, num_to_return)
        return {subreddit: selected_titles}
    else:
        print(f"--- Tool warning: Unknown subreddit '{subreddit}' requested. ---")
        return {subreddit: [f"Sorry, I don't have mock data for r/{subreddit}."]}

# Function to fetch news from multiple subreddits
def get_multi_subreddit_news(subreddits: Optional[List[str]] = None, limit: int = 3) -> Dict[str, List[str]]:
    """
    Fetches news from multiple subreddits.
    
    Args:
        subreddits: List of subreddit names to fetch news from. Defaults to ["worldnews", "news", "sports"]
        limit: Maximum number of posts to fetch per subreddit

    Returns:
        A dictionary with subreddit names as keys and lists of post titles as values.
    """
    if subreddits is None:
        subreddits = ["worldnews", "news", "sports"]
    
    results = {}
    for subreddit in subreddits:
        subreddit_results = get_subreddit_news(subreddit, limit)
        results.update(subreddit_results)
    
    return results

# Define the Agent
agent = Agent(
    name="reddit_scout_agent",
    description="A Reddit scout agent that searches for the most relevant posts in specified subreddits",
    model="gemini-1.5-flash-latest",
    instruction=(
        "You are the Reddit News Scout. Your primary task is to fetch and summarize news from various subreddits."
        "1. **Identify Intent:** Determine if the user is asking for news from specific subreddits."
        "2. **Determine Subreddits:** Identify which subreddit(s) to check:"
        "   - If no specific subreddit is mentioned, use the default set: 'worldnews', 'news', and 'sports'."
        "   - If specific subreddits are mentioned (e.g., 'politics', 'technology'), use those instead."
        "   - If both default and specific subreddits are requested, use both."
        "3. **Synthesize Output:** Present the exact list of titles returned by the tool."
        "4. **Format Response:** Present the information as a concise, bulleted list grouped by subreddit. Clearly state which subreddit each group of information came from. If the tool indicates an error or an unknown subreddit, report that message directly."
        "5. **MUST CALL TOOL:** You **MUST** call the `get_subreddit_news` tool for each subreddit mentioned, or use `get_multi_subreddit_news` for the default set. Do NOT generate summaries without calling the tool first."
    ),
    tools=[get_subreddit_news, get_multi_subreddit_news],
)
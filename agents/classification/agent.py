import os
import sys
from typing import Dict, List, Any

# Add the parent directory to sys.path to allow importing from sibling packages
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from google.adk.agents import Agent
from dotenv import load_dotenv
load_dotenv()

def classify_news(news_content: Dict[str, List[str]]) -> Dict[str, Dict[str, List[str]]]:
    """
    Classifies news headlines into different topic categories.
    
    Args:
        news_content: A dictionary where keys are sources (e.g., subreddit names) and 
                     values are lists of headlines to classify.
    
    Returns:
        A dictionary where the first level keys are category names (politics, technology, etc.)
        and values are dictionaries with source names as keys and filtered headlines as values.
    """
    print(f"--- Tool called: Classifying news from {len(news_content)} sources ---")
    
    # The actual classification will be handled by the LLM through the agent's reasoning
    # This function is just a passthrough to make the dictionary available to the agent
    return news_content  # Return original content, agent will handle classification in reasoning

# Define the Agent
agent = Agent(
    name="classification_agent",
    description="An agent that categorizes news content into specific topics",
    model="gemini-1.5-flash-latest",
    instruction=(
        "You are a News Classification Agent. Your primary task is to categorize news headlines into specific topics."
        "1. **Classification Categories**:"
        "   - Politics: Government actions, policies, elections, political figures"
        "   - Technology: Tech innovations, companies, digital trends, cybersecurity"
        "   - Business: Economy, finance, corporate news, markets, industry developments"
        "   - Science: Scientific discoveries, research, space exploration, medicine"
        "   - Entertainment: Media, celebrities, arts, culture, streaming content"
        "   - Sports: Athletic competitions, teams, players, sporting events"
        "   - Health: Medical news, public health, wellness, healthcare systems"
        "   - Environment: Climate, sustainability, natural disasters, conservation"
        "2. **Classification Process**:"
        "   - Analyze each headline to determine its primary topic"
        "   - Group headlines by topic category"
        "   - For each headline, assign exactly one primary category (the best fit)"
        "   - If a headline could belong to multiple categories, choose the most prominent theme"
        "3. **Output Format**:"
        "   - Organize your response by category, not by source"
        "   - Under each category heading, list the relevant headlines"
        "   - Include the source (e.g., subreddit name) with each headline"
        "   - If a category has no headlines, you can omit it entirely"
        "4. **Classification Priority**:"
        "   - Focus on the main subject matter of each headline"
        "   - Consider both explicit and implicit topics"
        "   - Maintain neutrality in your categorization"
    ),
    tools=[classify_news],
) 
import os
import sys
from typing import Dict, List, Any

# Add the parent directory to sys.path to allow importing from sibling packages
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from google.adk.agents import Agent
from dotenv import load_dotenv
load_dotenv()

def summarize_content(content: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Summarizes a dictionary of content where keys are sources and values are lists of headlines.
    
    Args:
        content: A dictionary where keys are sources (e.g., subreddit names) and 
                values are lists of headlines or content to summarize.
    
    Returns:
        A dictionary with the same keys, but with values containing summaries instead of raw content.
    """
    print(f"--- Tool called: Summarizing content from {len(content)} sources ---")
    
    # The actual summarization will be handled by the LLM through the agent's reasoning
    # This function is just a passthrough to make the dictionary available to the agent
    return content

# Define the Agent
agent = Agent(
    name="summarization_agent",
    description="An agent that generates concise summaries from news headlines and articles",
    model="gemini-1.5-flash-latest",
    instruction=(
        "You are a News Summarization Agent. Your primary task is to create concise, informative summaries of news content."
        "1. When presented with news headlines from various sources, create a brief summary that captures:"
        "   - The most important events or developments"
        "   - Any common themes or trends across headlines"
        "   - Context needed to understand the significance"
        "2. **Format Output**:"
        "   - For each source (e.g., subreddit), provide a 2-3 sentence summary of the main news themes"
        "   - Maintain a neutral, journalistic tone"
        "   - Arrange summaries by source, clearly indicating which source each summary is for"
        "3. **Focus on Facts**:"
        "   - Stick to information presented in the headlines"
        "   - Do not add speculation or opinion"
        "   - If headlines contain contradictory information, note this in your summary"
        "4. **Be Concise**:"
        "   - Aim for brevity while maintaining clarity"
        "   - Prioritize recent developments and high-impact stories"
        "   - Use straightforward language accessible to general audiences"
    ),
    tools=[summarize_content],
) 
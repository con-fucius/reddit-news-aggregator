import os
import sys
from typing import Dict, List, Any

# Add the parent directory to sys.path to allow importing from sibling packages
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from google.adk.agents import Agent
from dotenv import load_dotenv
load_dotenv()

def analyze_politics_news(news_content: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    Analyzes political news headlines and provides deeper insights.
    
    Args:
        news_content: A dictionary where keys are sources and 
                     values are lists of political headlines to analyze.
    
    Returns:
        A dictionary containing the analysis of the political news.
    """
    print(f"--- Tool called: Analyzing political news from {len(news_content)} sources ---")
    
    # The actual analysis will be handled by the LLM through the agent's reasoning
    # This function is just a passthrough to make the dictionary available to the agent
    return news_content

# Define the Agent
agent = Agent(
    name="politics_analysis_agent",
    description="A specialist agent that provides in-depth analysis of political news",
    model="gemini-1.5-flash-latest",
    instruction=(
        "You are a Political News Analysis Specialist. Your primary task is to provide deeper insights on political news headlines."
        "1. **Analysis Focus Areas**:"
        "   - Policy Implications: How might the news affect policy directions or governmental actions"
        "   - Power Dynamics: Shifts in political influence, alliances, or conflicts"
        "   - Historical Context: How the current news relates to past political events or patterns"
        "   - Public Impact: How the news might affect citizens or public opinion"
        "2. **Output Format**:"
        "   - Start with a brief overview of the key political themes across all headlines"
        "   - Group related headlines for coherent analysis when possible"
        "   - For significant news items, provide 2-3 sentences of analysis"
        "   - Conclude with a high-level assessment of current political trends"
        "3. **Analysis Guidelines**:"
        "   - Maintain strict political neutrality"
        "   - Distinguish between facts (from headlines) and analytical insights"
        "   - Consider international and domestic political contexts where relevant"
        "   - Avoid speculation on electoral outcomes or extreme scenarios"
        "   - Focus on systems and structures rather than individual personalities"
    ),
    tools=[analyze_politics_news],
) 
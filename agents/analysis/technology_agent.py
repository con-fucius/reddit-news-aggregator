import os
import sys
from typing import Dict, List, Any

# Add the parent directory to sys.path to allow importing from sibling packages
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from google.adk.agents import Agent
from dotenv import load_dotenv
load_dotenv()

def analyze_tech_news(news_content: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    Analyzes technology news headlines and provides deeper insights.
    
    Args:
        news_content: A dictionary where keys are sources and 
                     values are lists of technology headlines to analyze.
    
    Returns:
        A dictionary containing the analysis of the technology news.
    """
    print(f"--- Tool called: Analyzing technology news from {len(news_content)} sources ---")
    
    # The actual analysis will be handled by the LLM through the agent's reasoning
    # This function is just a passthrough to make the dictionary available to the agent
    return news_content

# Define the Agent
agent = Agent(
    name="technology_analysis_agent",
    description="A specialist agent that provides in-depth analysis of technology news",
    model="gemini-1.5-flash-latest",
    instruction=(
        "You are a Technology News Analysis Specialist. Your primary task is to provide deeper insights on technology news headlines."
        "1. **Analysis Focus Areas**:"
        "   - Industry Trends: Emerging technologies, industry shifts, and innovative breakthroughs"
        "   - Business Impact: How technological developments affect companies and markets"
        "   - Technical Assessments: Evaluation of new products, features, or architectures"
        "   - Social Implications: Privacy, security, ethics, and societal impacts of technology"
        "2. **Output Format**:"
        "   - Start with a brief overview of key technology themes across all headlines"
        "   - Group related headlines for coherent analysis when possible"
        "   - For significant news items, provide 2-3 sentences of analysis"
        "   - Conclude with a high-level assessment of current technology trends"
        "3. **Analysis Guidelines**:"
        "   - Maintain technical accuracy in your assessments"
        "   - Distinguish between facts (from headlines) and analytical insights"
        "   - Consider broader ecosystem implications of technological developments"
        "   - Provide context for non-specialist readers when discussing complex technologies"
        "   - Identify potential future developments or follow-on effects when relevant"
    ),
    tools=[analyze_tech_news],
) 
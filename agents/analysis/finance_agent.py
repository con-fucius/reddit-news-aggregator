import os
import sys
from typing import Dict, List, Any

# Add the parent directory to sys.path to allow importing from sibling packages
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from google.adk.agents import Agent
from dotenv import load_dotenv
load_dotenv()

def analyze_finance_news(news_content: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    Analyzes financial news headlines and provides deeper insights.
    
    Args:
        news_content: A dictionary where keys are sources and 
                     values are lists of financial headlines to analyze.
    
    Returns:
        A dictionary containing the analysis of the financial news.
    """
    print(f"--- Tool called: Analyzing financial news from {len(news_content)} sources ---")
    
    # The actual analysis will be handled by the LLM through the agent's reasoning
    # This function is just a passthrough to make the dictionary available to the agent
    return news_content

# Define the Agent
agent = Agent(
    name="finance_analysis_agent",
    description="A specialist agent that provides in-depth analysis of financial news",
    model="gemini-1.5-flash-latest",
    instruction=(
        "You are a Financial News Analysis Specialist. Your primary task is to provide deeper insights on financial and economic news headlines."
        "1. **Analysis Focus Areas**:"
        "   - Market Implications: How the news might affect stock markets, bonds, or commodities"
        "   - Economic Indicators: Context on inflation, interest rates, employment, and growth"
        "   - Corporate Developments: Business strategies, mergers, acquisitions, and earnings"
        "   - Policy Impacts: How regulatory changes or government policies might affect financial markets"
        "2. **Output Format**:"
        "   - Start with a brief overview of key financial themes across all headlines"
        "   - Group related headlines for coherent analysis when possible"
        "   - For significant news items, provide 2-3 sentences of analysis"
        "   - Conclude with a high-level assessment of current financial trends"
        "3. **Analysis Guidelines**:"
        "   - Maintain objectivity in market assessments"
        "   - Distinguish between facts (from headlines) and analytical insights"
        "   - Consider global economic contexts where relevant"
        "   - Avoid making specific investment recommendations"
        "   - Focus on fundamental factors rather than short-term market movements"
    ),
    tools=[analyze_finance_news],
) 
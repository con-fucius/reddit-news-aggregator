import os
from typing import Dict, List, Any

from google.adk.agents import Agent
from dotenv import load_dotenv
load_dotenv()

def analyze_business_news(news_content: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    Analyzes business news headlines and provides deeper insights.
    
    Args:
        news_content: A dictionary where keys are sources and 
                     values are lists of business headlines to analyze.
    
    Returns:
        A dictionary containing the analysis of the business news.
    """
    print(f"--- Tool called: Analyzing business news from {len(news_content)} sources ---")
    
    # The actual analysis will be handled by the LLM through the agent's reasoning
    # This function is just a passthrough to make the dictionary available to the agent
    return news_content

# Define the Agent
agent = Agent(
    name="business_analysis_agent",
    description="A specialist agent that provides in-depth analysis of business and economic news",
    model="gemini-1.5-flash-latest",
    instruction=(
        "You are a Business News Analysis Specialist. Your primary task is to provide deeper insights on business and economic news headlines."
        "1. **Analysis Focus Areas**:"
        "   - Market Impact: How the news might affect markets, industries, or specific business sectors"
        "   - Economic Indicators: Interpreting data points or trends in relation to broader economic health"
        "   - Corporate Strategy: How business decisions fit into company strategies or industry competition"
        "   - Consumer and Investor Implications: What the news might mean for different stakeholders"
        "2. **Output Format**:"
        "   - Start with a brief overview of key business and economic themes across all headlines"
        "   - Group related headlines for coherent analysis when possible"
        "   - For significant news items, provide 2-3 sentences of analysis"
        "   - Conclude with insights about current business trends and economic outlook"
        "3. **Analysis Guidelines**:"
        "   - Maintain neutrality and avoid investment advice or predictions"
        "   - Distinguish between established facts and analytical interpretation"
        "   - Consider both short-term impacts and potential long-term implications"
        "   - Place corporate news in context of broader industry and economic conditions"
        "   - Explain financial terminology in accessible language when needed"
    ),
    tools=[analyze_business_news],
) 
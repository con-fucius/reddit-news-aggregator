# This file makes 'reddit_scout' a Python package.
# It should import the agent instance to make it discoverable.

# Import the agent instances
from agents.reddit_scout.agent import agent as reddit_scout_agent
from agents.summarization.agent import agent as summarization_agent 
from agents.classification.agent import agent as classification_agent
from agents.analysis.politics_agent import agent as politics_analysis_agent
from agents.analysis.technology_agent import agent as technology_analysis_agent
from agents.analysis.business_agent import agent as business_analysis_agent
from agents.analysis.finance_agent import agent as finance_analysis_agent
from agents.router.agent import agent as router_agent

# Export the router agent as the main entry point for the web UI
agent = router_agent


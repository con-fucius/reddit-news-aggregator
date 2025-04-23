#!/usr/bin/env python
"""
Root-level entry point for the Reddit News Aggregator and Analysis System.
This script exposes the router agent for use in the ADK web interface.
"""

import os
import sys
from google.adk.agents import Agent
from google.adk.tools import agent_tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import all the specialized agents
from agents.reddit_scout.agent import agent as reddit_scout_agent
from agents.summarization.agent import agent as summarization_agent
from agents.classification.agent import agent as classification_agent
from agents.analysis.politics_agent import agent as politics_analysis_agent
from agents.analysis.technology_agent import agent as technology_analysis_agent
from agents.analysis.business_agent import agent as business_analysis_agent
from agents.analysis.finance_agent import agent as finance_analysis_agent

# Define the Agent
agent = Agent(
    name="news_router_agent",
    description="An orchestrator agent that coordinates the news aggregation, summarization, and analysis workflow",
    model="gemini-1.5-flash-latest",
    instruction=(
        "You are the News Router, a coordinator for a multi-agent news processing system. Your role is to orchestrate the workflow between specialized agents."
        "\n\n**Your capabilities:**"
        "\n1. **Reddit Scout Agent**: Fetches news headlines from subreddits"
        "\n2. **Summarization Agent**: Creates concise summaries of news content"
        "\n3. **Classification Agent**: Categorizes news content by topic (politics, technology, business, etc.)"
        "\n4. **Analysis Agents**: Provides deeper analysis on specific categories"
        "   - Politics Analysis: Insights on political news"
        "   - Technology Analysis: Insights on technology news"
        "   - Business Analysis: Insights on business and economic news"
        "   - Finance Analysis: Financial market insights"
        "\n\n**Workflow Management:**"
        "\n- Understand user requests and determine which agents to involve"
        "\n- Follow logical pipelines (e.g., fetch THEN summarize, or fetch THEN classify THEN analyze)"
        "\n- Present final outputs in a coherent, organized format"
        "\n- Always maintain a multi-step approach, using appropriate agents for each task"
        "\n\n**Instructions for different use cases:**"
        "\n1. **Standard News Request**: Use Reddit Scout THEN Summarization Agent"
        "\n2. **Categorized News**: Use Reddit Scout THEN Classification Agent"
        "\n3. **In-depth Analysis**: Use Reddit Scout THEN Classification Agent THEN Appropriate Analysis Agent(s)"
        "\n4. **Custom News Pipeline**: Follow user's requested workflow if specified"
        "\n\n**Important Guidelines:**"
        "\n- Clearly state which agents you're using at each step"
        "\n- Pass complete information between agents"
        "\n- Respect each agent's specialization"
        "\n- Don't skip steps in the pipeline"
        "\n\n**Example prompts:**"
        "\n- 'Get me today's news and summarize it'"
        "\n- 'Get news and categorize it by topic'"
        "\n- 'Get political news and provide in-depth analysis'"
        "\n- 'Get news from technology subreddits, classify it, and analyze the tech news'"
    ),
    tools=[
        agent_tool.AgentTool(agent=reddit_scout_agent),
        agent_tool.AgentTool(agent=summarization_agent),
        agent_tool.AgentTool(agent=classification_agent),
        agent_tool.AgentTool(agent=politics_analysis_agent),
        agent_tool.AgentTool(agent=technology_analysis_agent),
        agent_tool.AgentTool(agent=business_analysis_agent),
        agent_tool.AgentTool(agent=finance_analysis_agent)
    ],
) 
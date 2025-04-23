# This file makes 'analysis' a Python package.
# It should import the agent instances to make them discoverable.

# Import the agent instances
from .politics_agent import agent as politics_agent
from .technology_agent import agent as technology_agent
from .business_agent import agent as business_agent
from .finance_agent import agent as finance_agent 
#!/usr/bin/env python
"""
Command line entry point for the Reddit News Aggregator and Analysis System.
"""

from google.adk.run import run_cli
from agents import agent

if __name__ == "__main__":
    run_cli(agent) 
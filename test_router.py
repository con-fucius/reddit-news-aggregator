#!/usr/bin/env python
"""
Test script for the News Router Agent implementation.
This script runs the router agent to verify that it works as expected.
"""

import os
import sys
import subprocess

def main():
    """Main function to run the router agent."""
    
    # Print instructions for the user
    print("\n" + "="*80)
    print("News Router Agent Test")
    print("="*80)
    print("This script tests the News Router Agent, which orchestrates the news aggregation,")
    print("summarization, classification, and analysis workflow.")
    print("\nExample queries to test different pipeline functionalities:")
    print("1. Basic workflow: 'Get me today's news and summarize it'")
    print("2. Classification: 'Get news and categorize it by topic'")
    print("3. Deep analysis: 'Get political news and provide in-depth analysis'")
    print("4. Complex request: 'Get news from technology subreddits, classify it, and analyze the tech news'")
    print("="*80 + "\n")
    
    # Run the agent using the ADK CLI
    try:
        subprocess.run(["adk", "run", "agents/router"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running agent: {e}")
        return 1
    except FileNotFoundError:
        print("Error: 'adk' command not found. Make sure the ADK is installed and your virtual environment is activated.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 
# main.py
# This is the main entry point for the Supply Chain Risk Analyst AI.
# It handles the user interaction loop, takes user queries, and uses the agent to find answers.

import asyncio
from agent import SupplyChainAnalystAgent
from config import load_config

def display_welcome_message():
    """Prints a welcome message and instructions for the user."""
    print("\n--- Supply Chain Risk Analyst AI ---")
    print("Welcome! I am an AI agent designed to help you analyze supply chain risks.")
    print("You can ask me questions about potential disruptions, geopolitical impacts, port status, and more.")
    print("For example: 'What are the current supply chain risks for semiconductor manufacturing in Taiwan?'")
    print("Type 'exit' or 'quit' to end the session.\n")

async def main():
    """
    The main asynchronous function to run the agent.
    Initializes the agent and enters a loop to process user queries.
    """
    # Load configuration (e.g., API keys)
    load_config()

    # Create an instance of our specialized agent
    analyst_agent = SupplyChainAnalystAgent()

    # Display the initial welcome message to the user
    display_welcome_message()

    while True:
        try:
            # Prompt the user for their question
            user_query = input("Ask a question > ")

            # Check for exit commands
            if user_query.lower() in ["exit", "quit"]:
                print("Thank you for using the Supply Chain Analyst AI. Goodbye!")
                break

            # If the query is empty, prompt again
            if not user_query:
                continue

            # Run the agent with the user's query and print the result
            print("\nThinking...")
            result = await analyst_agent.run(user_query)
            print("\n--- Analysis ---")
            print(result)
            print("-" * 20 + "\n")

        except KeyboardInterrupt:
            print("\nSession interrupted by user. Exiting.")
            break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    # Run the main asynchronous event loop
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram terminated.")

# agent.py
# Contains the core logic for the AI agent.
# It uses a Language Model to reason, decide which tools to use, and formulate answers.

import os
from openai import AsyncOpenAI
from prompts import SYSTEM_PROMPT_TEMPLATE
from tools import SupplyChainNewsSearchTool

class SupplyChainAnalystAgent:
    """
    A reasoning agent specialized in analyzing supply chain risks.

    This agent uses an LLM to break down a user's query, use available tools
    to gather information, and synthesize an answer based on its findings.
    """
    def __init__(self, model="gpt-4o"):
        """
        Initializes the agent.
        Args:
            model (str): The name of the OpenAI model to use for reasoning.
        """
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        # The agent's "toolbox" contains all the tools it can use.
        self.tools = [SupplyChainNewsSearchTool()]

    async def run(self, query: str, max_steps: int = 5) -> str:
        """
        Runs the agent to answer a user's query.

        The agent operates in a loop:
        1. Thinks about what to do next.
        2. Chooses a tool to use.
        3. Executes the tool.
        4. Observes the result and repeats until it has an answer.

        Args:
            query (str): The user's question.
            max_steps (int): The maximum number of steps the agent can take.

        Returns:
            str: The final answer to the user's query.
        """
        # Format the system prompt with the tools the agent can use
        system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
            tools_summary=self._get_tools_summary(),
            tools_details=self._get_tools_details()
        )

        # Initialize the conversation history
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"My question is: {query}"}
        ]

        for step in range(max_steps):
            print(f"--- Step {step + 1} ---")
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.0,
            )
            assistant_message = response.choices[0].message
            messages.append(assistant_message)

            # Check if the assistant's message contains the final answer
            if "<answer>" in assistant_message.content:
                final_answer = self._extract_content(assistant_message.content, "answer")
                print("Agent has formulated the final answer.")
                return final_answer

            # If not, the agent must be thinking about using a tool
            if "<tool>" in assistant_message.content:
                tool_name = self._extract_content(assistant_message.content, "tool")
                tool_input = self._extract_content(assistant_message.content, "tool_input")
                print(f"Agent wants to use tool: {tool_name} with input: '{tool_input}'")

                # Find and execute the chosen tool
                tool = self._find_tool(tool_name)
                if tool:
                    tool_output = await tool.use(tool_input)
                    observation = f"<observation>\n{tool_output}\n</observation>"
                else:
                    observation = f"<observation>\nTool '{tool_name}' not found.\n</observation>"

                print(f"Observation: {observation[:200]}...") # Print snippet of observation
                messages.append({"role": "user", "content": observation})
            else:
                # If the agent doesn't provide an answer or use a tool, it might be stuck.
                return "The agent could not find an answer or decide on the next step."

        return "The agent reached the maximum number of steps without finding an answer."

    def _get_tools_summary(self) -> str:
        """Generates a summary of available tools for the prompt."""
        return "\n".join([f"- {tool.name}: {tool.description}" for tool in self.tools])

    def _get_tools_details(self) -> str:
        """Generates detailed descriptions of available tools for the prompt."""
        return "\n".join([tool.details for tool in self.tools])

    def _find_tool(self, name: str):
        """Finds a tool instance by its name."""
        for tool in self.tools:
            if tool.name == name:
                return tool
        return None

    @staticmethod
    def _extract_content(text: str, tag: str) -> str:
        """Extracts content from within a given XML-like tag."""
        try:
            start_tag = f"<{tag}>"
            end_tag = f"</{tag}>"
            start_index = text.index(start_tag) + len(start_tag)
            end_index = text.index(end_tag)
            return text[start_index:end_index].strip()
        except ValueError:
            return ""

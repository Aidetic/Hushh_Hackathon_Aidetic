import re
import json
from abc import ABC


class LlmBase(ABC):
    """
    Abstract base class for LLM wrappers.

    Provides a default `infer` method (meant to be overridden) and a helper to parse LLM JSON output.
    """

    def __init__(self):
        """
        Initialize the base LLM class.
        """
        super().__init__()

    def infer(self, input):
        """
        Dummy inference method to be overridden by subclasses.

        Args:
            input (str): Input prompt or data for the LLM.

        Returns:
            str: Placeholder response.
        """
        return f"LLM response for {input}"

    def convert_to_json(self, text):
        """
        Converts a raw LLM response string to a JSON object, removing optional markdown-style code blocks.

        Args:
            text (str): The raw string response from the LLM.

        Returns:
            dict: Parsed JSON object.

        Raises:
            json.JSONDecodeError: If the string is not valid JSON.
        """
        cleaned = re.sub("```json", "", text)
        cleaned = re.sub("```", "", cleaned)
        # print("json string after cleaning")
        # print(cleaned)
        return json.loads(cleaned)
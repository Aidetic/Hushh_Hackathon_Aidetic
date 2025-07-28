from core.tools.base import Tool
from core.llm.llm import Llm

class AskLLM(Tool):
    def __init__(self):
        super().__init__()
        self.llm = Llm()

    def __call__(self, user_id, query: str):
        """
        ask_llm(query: str) -> str

        **IMPORTANT USAGE NOTE**

        This function is ONLY to be used when:
        - All required data and context are already gathered and available.
        - The LLM is needed purely to analyze, summarize, generate, or compose an answer based on this *fully-supplied* information.

        **DO NOT use this tool to ask open-ended questions or to "figure things out" when data is missing.**
        - Using ask_llm with insufficient data or context WILL result in unreliable or hallucinated outputs.
        - This function is NOT a replacement for retrieving, looking up, or fetching real data—do NOT use it as a shortcut for upstream work.

        Typical usage: Last step of a plan, *after* all necessary facts have been assembled from tools and context, e.g.:
        - Summarizing a known list of transactions.
        - Generating a message from already-extracted user preferences.
        - Filtering or ranking items based on a provided data set.

        Params:
            query (str): The prompt or instruction for the LLM, which must contain all data it needs for a correct response.

        Returns:
            str: The LLM's output string based ONLY on the data provided in the query.
        """
        return self.llm.infer(query + "NOTE: NEVER RESPOND IN A QUESTION, ALWAYS RESPOND WITH A CLEAR DIRECT ANSWER")

    def __repr__(self):
        return self.__call__.__doc__

ask_llm = AskLLM()

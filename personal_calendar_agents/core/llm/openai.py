from core.llm.base import LlmBase
from openai import OpenAI

class LlmOpenai(LlmBase):

    def __init__(self):
        super().__init__()
        self.client = OpenAI()

    def infer(self, prompt):
        response = self.client.responses.create(
            model="gpt-4.1",
            input=prompt
        )
        return response.output_text
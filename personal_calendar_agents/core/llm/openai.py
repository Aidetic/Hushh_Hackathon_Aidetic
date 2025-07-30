from core.llm.base import LlmBase
from openai import OpenAI
from core.settings import settings
import json

class LlmOpenai(LlmBase):

    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key = settings.OPENAI_API_KEY)

    def infer(self, prompt, get_json=False):
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )
        output = response.output_text
        if get_json:
            return json.loads(output)
        return output

if __name__ == "__main__":
    llm = LlmOpenai()
    print(llm.infer("Create a json list of first 5 alphabets"))
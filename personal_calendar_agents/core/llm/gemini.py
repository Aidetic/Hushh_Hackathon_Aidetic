from google import genai
from core.llm.base import LlmBase
from google.genai import types
from core.settings import settings

class LlmGemini(LlmBase):
    """
    Wrapper class for interacting with Google's Gemini model via the genai client.

    This class initializes a Gemini client using API credentials from the settings
    and provides an `infer` method to send prompts and optionally images for processing,
    returning the model's response along with token usage statistics.
    """

    def __init__(self):
        """
        Initializes the Gemini LLM client using API credentials from the settings.
        """
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.gemini_model_name = settings.GEMINI_MODEL_NAME

    def infer(
        self,
        prompt_str,
        get_json=False,
    ):
        """
        Sends a prompt and optionally an image to the Gemini model and returns the response.

        Args:
            prompt_str (str): The text prompt to send to the model.
            image (Optional): An optional image to include in the request.
            sys_prompt (Optional): System prompt (currently unused).
            get_json (bool): Whether to convert the response to JSON (default: True).

        Returns:
            Tuple:
                - llm_response (str or dict): The raw or JSON-parsed response from Gemini.
                - usage (dict): A dictionary with token usage details:
                    * input_text_token_count
                    * image_token_count
                    * output_text_token_count
        """
        contents_list = [prompt_str]
        
        gemini_api_response = self.client.models.generate_content(
            model=self.gemini_model_name, contents=contents_list,
            config=types.GenerateContentConfig( top_p= 0, top_k=1)
        )


        llm_response = gemini_api_response.candidates[0].content.parts[0].text

        try:        
            if get_json:
                llm_response = self.convert_to_json(llm_response)
        except:
            print("Error decoding response: ")
            print(llm_response)
            print("Retrying: ")
            return self.infer(prompt_str=prompt_str)
        
        return llm_response
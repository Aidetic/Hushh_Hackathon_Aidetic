from core.tool_caller.base import ToolCallerBase
from core.llm.llm import Llm

class ToolCaller(ToolCallerBase):
    def __init__(
            self, 
            username,
            tools_pkg="core.tools",
        ):
        super().__init__(tools_pkg)
        self.username = username
        self.llm = Llm()

    def __call__(self, query):
        response = self.llm.infer(
            self.PROMPT.format(
                query=query,
                tool_list=self.list_tools(),
            ),
            get_json=True
        )

        func_name = response.get('func_name')
        args = response.get('args', {}) or {}
        args["user_id"] = self.username
        
        if func_name not in self.tools:
            if not isinstance(response, dict):
                return response
            return response.get("response") or response
                
        result = self.tools[func_name](**args)

        compiled_result = result
        
        return compiled_result

# Example usage:
if __name__ == "__main__":
    tc = ToolCaller("pandeygag78934@gmail.com")
    #print(tc("Show my calendar events for this week"))
    print("Here are the tools you asked for: ",tc.tools.keys())

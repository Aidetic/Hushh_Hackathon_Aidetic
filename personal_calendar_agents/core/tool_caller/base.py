import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import importlib
from pathlib import Path

from core.llm.llm import Llm
from core.prompts import args_builder

class ToolCallerBase:

    def __init__(self, tools_pkg="core.tools"):
        self.llm = Llm()
        self.PROMPT = args_builder.prompt
        self.tools_pkg = tools_pkg
        self.tools = self.get_tools()

    def get_tools(self):
        """Dynamically import all tools in self.tools_pkg and return a dict of name: callable."""
        tools = {}
        package_dir = Path(importlib.import_module(self.tools_pkg).__file__).parent
        for pyfile in package_dir.glob("*.py"):
            if pyfile.name.startswith("_") or pyfile.name == "__init__.py":
                continue
            mod_name = f"{self.tools_pkg}.{pyfile.stem}"
            try:
                mod = importlib.import_module(mod_name)
                tool = getattr(mod, pyfile.stem, None)
                if tool and callable(tool) and hasattr(tool, '__repr__'):
                    tools[pyfile.stem] = tool
            except Exception as e:
                print(f"Failed to import {mod_name}: {e}")
        return tools

    def list_tools(self):
        """Returns a nicely formatted string of all tools and their docstrings for the prompt."""
        return "\t\t".join([
            f"{name}: {str(tool)}" for name, tool in self.tools.items()
        ])

    def __call__(self, query):
        
        response = self.llm.infer(
            self.PROMPT.format(
                query=query,
                tool_list=self.list_tools(),
            ),
            get_json=True
        )

        # Defensive: check function exists
        func_name = response.get('func_name')
        args = response.get('args', {})
        if func_name not in self.tools:
            raise Exception(f"Function '{func_name}' not found in tool registry.")

        result = self.tools[func_name](**args)
        return result

# Example usage
if __name__ == "__main__":
    tc = ToolCallerBase()
    print(tc.tools)
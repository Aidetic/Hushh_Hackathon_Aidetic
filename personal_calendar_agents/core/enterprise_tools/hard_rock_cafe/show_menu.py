from core.tools.base import Tool
import os
import json

class ShowMenu(Tool):
    def __call__(self, base_dir="./data/agents/enterprise/hard_rock_cafe", user_id = None):
        """
        show_menu(base_dir: str = "./data/agents/enterprise/hard_rock_cafe") -> list

        Returns the full menu for Hard Rock Cafe as a list of menu item dicts.
        """
        path = os.path.join(base_dir, "menu.json")
        with open(path, "r") as f:
            menu = json.load(f)
        return menu

    def __repr__(self):
        return self.__call__.__doc__

show_menu = ShowMenu()

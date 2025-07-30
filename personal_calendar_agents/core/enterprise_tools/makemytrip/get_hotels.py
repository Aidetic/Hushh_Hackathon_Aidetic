from core.tools.base import Tool
import os
import json

class GetHotels(Tool):
    def __call__(self, base_dir=f"{os.getenv('DATABASE')}/agents/enterprise/makemytrip", user_id = None):
        """
        get_hotels() -> list
        Returns a list of hotel dicts.
        Suitable when someone wants to book hotels for travel
        """
        path = os.path.join(base_dir, "hotels.json")
        with open(path, "r") as f:
            hotels = json.load(f)
        return hotels

    def __repr__(self):
        return self.__call__.__doc__

get_hotels = GetHotels()

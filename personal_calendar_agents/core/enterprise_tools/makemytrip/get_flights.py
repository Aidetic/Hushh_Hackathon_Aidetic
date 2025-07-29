from core.tools.base import Tool
import os
import json

class GetFlights(Tool):
    def __call__(self, base_dir="./data/agents/enterprise/makemytrip", user_id = None):
        """
        get_flights() -> list
        Returns a list of flight dicts.
        Suitable when someone wants to schedule flights for travel
        """
        path = os.path.join(base_dir, "flights.json")
        with open(path, "r") as f:
            flights = json.load(f)
        return flights

    def __repr__(self):
        return self.__call__.__doc__

get_flights = GetFlights()

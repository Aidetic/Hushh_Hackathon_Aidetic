from core.tools.base import Tool
import os
import json

class FindTable(Tool):
    def __call__(self, date, party_size, base_dir="./data/agents/enterprise/hard_rock_cafe", user_id = None):
        """
        find_table(date: str, party_size: int, base_dir: str = "./data/agents/enterprise/hard_rock_cafe") -> list

        Finds tables available on a given date for at least the given party size.
        Returns a list of matching table dicts.
        """
        path = os.path.join(base_dir, "tables.json")
        with open(path, "r") as f:
            tables = json.load(f)
        results = [t for t in tables if party_size <= t["capacity"] and date in t["available_dates"]]
        return results

    def __repr__(self):
        return self.__call__.__doc__

find_table = FindTable()

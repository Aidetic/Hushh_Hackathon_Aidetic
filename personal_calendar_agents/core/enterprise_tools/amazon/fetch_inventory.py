from core.tools.base import Tool
import os
import json

class FetchInventory(Tool):
    def __call__(self, base_dir="./data/agents/enterprise/amazon", user_id = None):
        """
        fetch_inventory() -> list

        Fetches Amazon inventory for items.
        Returns a list of product dicts.
        """
        path = os.path.join(base_dir, "inventory.json")
        with open(path, "r") as f:
            inventory = json.load(f)
        return inventory

    def __repr__(self):
        return self.__call__.__doc__

fetch_inventory = FetchInventory()

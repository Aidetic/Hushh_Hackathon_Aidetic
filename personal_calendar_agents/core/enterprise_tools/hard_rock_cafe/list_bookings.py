from core.tools.base import Tool
import os
import json

class ListBookings(Tool):
    def __call__(self, user_id, base_dir="./data/agents/enterprise/hard_rock_cafe"):
        """
        list_bookings(user_id: str, base_dir: str = "./data/agents/enterprise/hard_rock_cafe") -> list

        Returns a list of all bookings for the specified user at Hard Rock Cafe.
        """
        path = os.path.join(base_dir, "booking.json")
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            bookings = json.load(f)
        return [b for b in bookings if b["user_id"] == user_id]

    def __repr__(self):
        return self.__call__.__doc__

list_bookings = ListBookings()

from core.tools.base import Tool
import os

class GetPreferences(Tool):
    def __call__(self, user_id, base_dir=f"{os.getenv('DATABASE')}/agents/personal"):
        """
        For any gifting, purchasing, planning related queries about YOURSELF AS AN AI AGENT or HUMAN, these are NECESSARY.
        get_preferences(user_id: str, base_dir: str = "./data/agents/personal") -> str
        Returns the full content of preferences.txt for the user.
        Params:
            user_id: Email or unique identifier of the user.
            base_dir: Root directory where user data is stored.
        Returns:
            Preferences as plain text.

        These are general information about the user.
        """
        import os
        path = os.path.join(base_dir, user_id, "preferences.txt")
        if not os.path.exists(path):
            return ""
        with open(path, "r") as f:
            return f.read()
    def __repr__(self):
        return self.__call__.__doc__
get_preferences = GetPreferences()

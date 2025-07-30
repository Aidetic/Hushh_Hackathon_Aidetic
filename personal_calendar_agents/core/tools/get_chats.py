from core.tools.base import Tool
import os

class GetChats(Tool):
    def __call__(self, user_id, base_dir=f"{os.getenv('DATABASE')}/agents/personal"):
        """

        FOR ANY QUERY RELATED TO CHATS, ENSURE THAT THIS IS CALLED AND CHATS ARE LOADED

        get_chats(user_id: str, base_dir: str = "./data/agents/personal") -> str
        Returns a chats in a string for the specified user_id.
        Params:
            user_id: Email or unique identifier of the user.
            base_dir: Root directory where user data is stored.
        Returns:
            Chats as a single string.
        """
        import os
        path = os.path.join(base_dir, user_id, "chat.txt")
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            return f.read()
    def __repr__(self):
        return self.__call__.__doc__

get_chats = GetChats()
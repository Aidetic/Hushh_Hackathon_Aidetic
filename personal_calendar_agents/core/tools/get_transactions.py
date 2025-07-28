from core.tools.base import Tool


class GetTransactions(Tool):
    def __call__(self, user_id, base_dir="./data/agents/personal"):
        """
        get_transactions(user_id: str, base_dir: str = "./data/agents/personal") -> list
        Returns a list of transactions for the specified user_id.
        Params:
            user_id: Email or unique identifier of the user.
            base_dir: Root directory where user data is stored.
        Returns:
            List of transactions (dict).
        """
        import os, json
        path = os.path.join(base_dir, user_id, "transactions.json")
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            return json.load(f)
    def __repr__(self):
        return self.__call__.__doc__
get_transactions = GetTransactions()
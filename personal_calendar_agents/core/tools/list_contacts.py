from core.tools.base import Tool
import os
import json

class ListContacts(Tool):
    """
    list_contacts(user_id: str, base_dir: str = "./data/agents/personal") -> list

    Returns the full list of contacts for the specified user.

    Params:
        user_id: Email or unique identifier of the user whose contacts should be listed.
        base_dir: Root directory where user data is stored.

    Returns:
        List of contact dictionaries (e.g., [{ "name": ..., "email": ... }, ...]).
        Returns an empty list if no contacts are found.

        IN CASE OF CONTACTS BEING ENTEPRISE AGENTS, THE EMAIL IS A SINGLE WORD WITHOUT ANY @ SIGN.
        
    """

    def __call__(self, user_id, base_dir="./data/agents/personal"):
        """
    list_contacts(user_id: str, base_dir: str = "./data/agents/personal") -> list

    Returns the full list of contacts for the specified user.

    Params:
        user_id: Email or unique identifier of the user whose contacts should be listed.
        base_dir: Root directory where user data is stored.

    Returns:
        List of contact dictionaries (e.g., [{ "name": ..., "email": ... }, ...]).
        Returns an empty list if no contacts are found.
    """
        contacts_path = os.path.join(base_dir, user_id, "contacts.json")
        if not os.path.exists(contacts_path):
            return []
        with open(contacts_path, "r") as f:
            contacts = json.load(f)
        return contacts

    def __repr__(self):
        return self.__call__.__doc__

list_contacts = ListContacts()

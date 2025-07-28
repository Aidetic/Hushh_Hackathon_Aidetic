from core.llm.llm import Llm
from core.tools.base import Tool
from core.agent_manager.agent import Agent
from core.agent_manager.enterprise_registry import ENTERPRISE_AGENTS
from core.prompts import chat_conclusion

def section(title, icon=None):
    bar = "━" * 36
    # return f"\t{bar}\t{icon+' ' if icon else ''}**{title}**\t{bar}"
    return f"{bar} {icon+' ' if icon else ''}**{title}** {bar}"

class ContactAgent(Tool):
    
    def __init__(self, max_turns=12):
        super().__init__()
        self.llm = Llm()
        self.max_turns = max_turns
        self.chat_conclusion_prompt = chat_conclusion.prompt
    
    def __call__(
        self, 
        initiator_agenda: str,
        responder_agent_email: str,
        user_id: str,
    ):
        """
            Allows the responder_agent to respond to the initiator_agenda.

            IMPORTANT:
            - This function is ONLY useful if responder_agent_email is already known.
            - Always run get_contacts first to fetch the correct email before using this.
            - The initiator_agenda must be written in first person, directly stating what you want the responder to do.
            - The agenda must include ALL necessary details and contextual information the responder might need to act.  
            Be specific, data-rich, and make it easy for the responder to understand and complete the request.
            Example: "I want to ask you, XYZ, about ... [with all context and specifics]"

            Args:
                initiator_agenda (str): The agenda, written in first person, including all required details and context to fulfill the request.
                responder_agent_email (str): The responder agent’s email (must be pre-fetched).

            Returns:
                str: The response.
        """

        responder_agent = (
            Agent(responder_agent_email) if "@" in responder_agent_email
            else ENTERPRISE_AGENTS[responder_agent_email]
        )


        # The main loop
        # yield section(f"{responder_agent.username} Planning Step {n_turns+1}", "🤖")
        # yield f"{responder_agent.username} is processing: {initiator_agenda}"
        yield {"title": "logs", "content": f"{responder_agent.username} is processing: {initiator_agenda}"}

        responder_reply = responder_agent.handle_message(
            history="",
            message=initiator_agenda,
            agenda=None,
        )
        yield {"title": f"logs", "content": " ".join(str(responder_reply).splitlines())}

        return responder_reply
        
    def __repr__(self):
        return self.__call__.__doc__

contact_agent = ContactAgent()

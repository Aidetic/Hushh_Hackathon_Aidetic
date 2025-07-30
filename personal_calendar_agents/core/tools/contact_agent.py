from core.llm.llm import Llm
from core.tools.base import Tool
from core.agent_manager.agent import Agent
from core.agent_manager.enterprise_registry import ENTERPRISE_AGENTS
from core.prompts import chat_conclusion
import json


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
            Agent(responder_agent_email)
            if "@" in responder_agent_email
            else ENTERPRISE_AGENTS[responder_agent_email]
        )

        # The main loop
        # yield section(f"{responder_agent.username} Planning Step {n_turns+1}", "🤖")
        # yield f"{responder_agent.username} is processing: {initiator_agenda}"
        # yield json.dumps(
        #     {
        #         "title": "logs",
        #         "content": f"{responder_agent.username} is processing: {initiator_agenda}",
        #     },
        #     ensure_ascii=False,
        # )
        yield json.dumps(f"{responder_agent.username} is processing: {initiator_agenda}", ensure_ascii=False)

        responder_reply_steps = list(
            responder_agent.handle_message(
                history="",
                message=initiator_agenda,
                agenda=None,
            )
        )
        for step in responder_reply_steps:
            # Indent for subagent clarity
            # yield "\t> ".join(str(step).splitlines())
            # yield json.dumps(
            #     {"title": f"logs", "content": " ".join(str(step).splitlines())},
            #     ensure_ascii=False,
            # )
            print(json.loads(" ".join(str(step).splitlines()))["content"], "2" * 100)
            yield json.loads(" ".join(str(step).splitlines()))["content"]
            
        responder_reply_text = (
            responder_reply_steps[-1] if responder_reply_steps else ""
        )
        print(responder_reply_text, type(responder_reply_text), "3" * 100)
        if isinstance(responder_reply_text, dict) and "content" in responder_reply_text:
            responder_reply_text = responder_reply_text["content"]
        else:
            responder_reply_text = json.loads(responder_reply_text)["content"]
        print(responder_reply_text, type(responder_reply_text), "4" * 100)
        return responder_reply_text

    def __repr__(self):
        return self.__call__.__doc__


contact_agent = ContactAgent()

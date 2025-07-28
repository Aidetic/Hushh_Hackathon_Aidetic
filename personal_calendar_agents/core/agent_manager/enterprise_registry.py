from core.agent_manager.agent import Agent

# Registry of all enterprise agents: key = agent name, value = Agent object
ENTERPRISE_AGENTS = {
    "amazon": Agent(username="amazon", tools_pkg="core.enterprise_tools.amazon"),
    "hard_rock_cafe": Agent(username="hard_rock_cafe", tools_pkg="core.enterprise_tools.hard_rock_cafe"),
    "makemytrip": Agent(username="makemytrip", tools_pkg="core.enterprise_tools.makemytrip"),
}

if __name__ == "__main__":
    print("Available Enterprise Agents:", list(ENTERPRISE_AGENTS.keys()))
    agent = ENTERPRISE_AGENTS["amazon"]
    result = agent.handle_message("Show me all gifts under 1500 rupees")
    print("Amazon agent response:", result)

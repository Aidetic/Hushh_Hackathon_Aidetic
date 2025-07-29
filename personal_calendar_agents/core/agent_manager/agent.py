from core.tool_caller.nl_tool_interface import ToolCaller
from core.llm.llm import Llm
from core.prompts import actions_planner, step_execution
import types
import json

def section(title, icon=None):
    bar = "━" * 36
    # return f"\t{bar}\t{icon+' ' if icon else ''}**{title}**\t{bar}"
    return f"{bar} {icon + ' ' if icon else ''}**{title}** {bar}"

def format_plan(plan):
    if isinstance(plan, list):
        # return "\t" + "\t".join([f"  {i+1}. {step}" for i, step in enumerate(plan)])
        return "\n".join([f"  {i+1}. {step}" for i, step in enumerate(plan)])
    return f"{plan}"
    # return f"\t{plan}"

class Agent:
    def __init__(self, username, tools_pkg=None):
        self.username = username
        if tools_pkg:
            self.toolCaller = ToolCaller(username=username, tools_pkg=tools_pkg)
        else:
            self.toolCaller = ToolCaller(username=username)
        self.llm = Llm()
        self.step_execution_prompt = step_execution.prompt
        self.planner_prompt = actions_planner.prompt

    def handle_message(self, message, history=None, agenda=None):
        tools_list = self.toolCaller.get_tools()
        tools_text = "\t    ".join([f"{k}: {str(v)}" for k, v in tools_list.items()])
        llm_input = self.planner_prompt.format(
            name=self.username,
            history=history,
            message=message,
            tools_text=tools_text,
            enterprise_agents="amazon, makemytrip, hard_rock_cafe"
        )
        plan = self.llm.infer(llm_input, get_json=True)
        # Show plan section
        # yield section(f"Agent Plan for {self.username}", "🧠")
        yield json.dumps({"title": "logs", "content": section(f"Agent Plan for {self.username}", "🧠")}, ensure_ascii=False)
        # yield format_plan(plan)
        yield json.dumps({"title": "logs", "content": format_plan(plan)}, ensure_ascii=False)
        # Flatten toolcall generators
        yield from self.execute_plan(plan)
    
    def stringify_step_responses(self, step_responses):
        resp = ""
        for step in step_responses:
            resp += f"\tStep {step['step']+1}: {step['step_instruction']}\t"
            resp += f"    ↳ Response: {step['step_response']}\t"
        return resp

    def execute_plan(self, plan):
        plan_step_responses = []
        for step_idx, step in enumerate(plan):
            # yield section(f"Executing {step_idx+1}", "🔎")
            yield json.dumps({"title": "logs", "content": section(f"Executing {step_idx+1}", "🔎")}, ensure_ascii=False)
            # yield f"**→ Executing:** {step}"
            yield json.dumps({"title": "logs", "content": f"**→ Executing:** {step}"}, ensure_ascii=False)
            step_prompt = self.step_execution_prompt.format(
                plan=plan,
                execution_logs=self.stringify_step_responses(plan_step_responses),
                step=step
            )
            response = self.toolCaller(step_prompt)
            # If the tool returns a generator (e.g. contact_agent), flatten/yield its steps
            if isinstance(response, types.GeneratorType):
                for substep in response:
                    # Indent subagent yields
                    # yield "\t> ".join(str(substep).splitlines())
                    yield json.dumps({"title": "logs", "content": " ".join(str(substep).splitlines())}, ensure_ascii=False)
                # Use last substep's content as result
                last_content = str(substep) if 'substep' in locals() else ""
            else:
                last_content = str(response)
            # yield section(f"Result of Step {step_idx+1}", "📣")
            yield json.dumps({"title": "logs", "content": section(f"Result of Step {step_idx+1}", "📣")}, ensure_ascii=False)
            # yield last_content
            yield json.dumps({"title": "logs", "content": last_content}, ensure_ascii=False)
            plan_step_responses.append({
                "step": step_idx,
                "step_instruction": step,
                "step_response": last_content
            })
        # Final summary
        # yield section("Final Result", "🏁")
        # yield {"title": "logs", "content": section("Final Result", "🏁")}
        # yield plan_step_responses[-1]['step_response'] if plan_step_responses else ""
        yield json.dumps({
            "title": "report",
            "content": plan_step_responses[-1]['step_response'] if plan_step_responses else ""
        }, ensure_ascii=False)

def test_agent_instruction():
    agent = Agent("pandeygag78934@gmail.com")
    for event in agent.handle_message("Ask Nayna what she likes and buy something for her from amazon under inr 1k"):
        print(event)
        print()

if __name__ == '__main__':
    test_agent_instruction()

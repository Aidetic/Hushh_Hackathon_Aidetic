from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Generator
from fastapi.responses import StreamingResponse

import sys
import os
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.agent_manager.agent import Agent

app = FastAPI(title="Personal Calendar Agents API")

# CORS for your frontend origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://164.52.195.168:3011",
        "https://agents.hushh.aidetic.in"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgentInstruction(BaseModel):
    instruction: str
    user_email: str

def agent_yield_response(instruction: str, user_email: str = "pandeygag78934@gmail.com") -> Generator[str, None, None]:
    """
    Yields each step (as a string) from the agent's reasoning for the given instruction and user.
    """
    agent = Agent(user_email)
    for step in agent.handle_message(instruction):
        # Each 'step' is already a nicely formatted string
        # yield step + "\t"   # newline for frontend chunking
        yield json.dumps(step, ensure_ascii=False) + "\n"
        # yield step["content"] + " "   # newline for frontend chunking

@app.post("/run_agent")
def run_agent(
    query: AgentInstruction = Body(..., description="Instruction and user email for the agent.")
):
    """
    Endpoint to run a reasoning agent with a given instruction and user context.

    Request:
    {
        "instruction": "Your natural language goal or prompt.",
        "user_email": "user@example.com"
    }
    """
    try:
        return StreamingResponse(agent_yield_response(query.instruction, query.user_email), media_type="text/plain")
    except Exception as e:
        print(f"Error while evaluating query: {str(e)}")
        raise Exception(f"Error: {str(e)}")
# Optional: Quick local dev run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8903)

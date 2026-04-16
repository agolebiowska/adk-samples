from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types

from .config import config
from .prompt import get_prompt
from .tools.artifact_tools import save_artifact


root_agent = LlmAgent(
    name="sdlc_task_planner_agent",
    model=config.default_llm,
    description="Agent that manages task creation and outputs a detailed MR plan based on technical design.",
    instruction=get_prompt(),
    tools=[],
)

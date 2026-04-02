from google.adk.agents import LlmAgent
from .prompt import get_prompt
from .config import config
from .tools.artifact_tools import save_artifact

root_agent = LlmAgent(
    name="sdlc_task_planner_agent",
    model=config.default_llm,
    description="Agent that manages task creation and outputs a detailed MR plan based on technical design.",
    instruction=get_prompt(),
    tools=[save_artifact],
)

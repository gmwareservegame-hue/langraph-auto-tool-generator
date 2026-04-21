import json
from infrastructure.llm.gemini import get_llm
from domain.models.generated_tool import GeneratedTool
from application.tool_generator.prompt import tool_generator_prompt_v2
import logging

logger = logging.getLogger(__name__)


class ToolGenerator:

    def __init__(self):
        self.llm = get_llm()

    def generate(self, goal: str, context: str) -> GeneratedTool:
        prompt = tool_generator_prompt_v2.format(goal=goal, context=context)

        logger.debug(f"Invoking ToolGenerator LLM: \n\n{prompt}")

        llm_structured = self.llm.with_structured_output(GeneratedTool)
        response = llm_structured.invoke(prompt)

        logger.debug(f"ToolGenerator LLM Response: \n\n{response.model_dump_json()}")

        return response
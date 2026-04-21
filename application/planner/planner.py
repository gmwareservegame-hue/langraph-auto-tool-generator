import json
from domain.models.plan import Plan
from domain.models.goal import Goal
from domain.tools.registry import ToolRegistry
from infrastructure.llm.gemini import get_llm
from application.planner.tool_serializer import serialize_tools
from infrastructure.llm.response_wrappers.response_wrappers import GeminiFlashLite_3_1_ResponseWrapper

import logging

logger = logging.getLogger(__name__)

class Planner:

    def __init__(self, registry: ToolRegistry):
        self.registry = registry
        self.llm = get_llm()

    def create_plan(self, goal: Goal) -> Plan:
        tools = serialize_tools(self.registry.list())

        prompt = f"""
Eres un planner de IA.

OBJETIVO:
{goal.description}

TOOLS DISPONIBLES:
{json.dumps(tools, indent=2)}

REGLAS:
- Siempre usa una tool adecuada si existe
- Si no existe una tool adecuada, indica que se necesita crear una nueva
- Evita resolver el problema directamente sin tools
- tool_name NUNCA puede ser null
- Si ninguna sirve, indica explícitamente: "NO_TOOL"


Devuelve un plan en JSON con este formato:
{{
  "steps": [
    {{
      "tool_name": "string",
      "input_data": {{}}
    }}
  ]
}}

Solo devuelve JSON válido.
"""
        logger.debug(f"Invoking Planner LLM: \n\n{prompt}")
        llm_structured = self.llm.with_structured_output(Plan)
        response = llm_structured.invoke(prompt)
        # response = GeminiFlashLite_3_1_ResponseWrapper(response)
        logger.debug(f"Planner LLM Response: \n\n{response.model_dump_json()}")

        return response
from application.tool_factory.tool_factory import ToolFactory
from application.tool_generator.tool_generator import ToolGenerator
from application.tool_validator.tool_validator import ToolValidator
from domain.models.state import AgentState
from domain.tools.registry import ToolRegistry
from utils.logging import log_block


def build_tool_generation_node(generator: ToolGenerator, validator: ToolValidator, factory: ToolFactory, registry: ToolRegistry):

    @log_block(__name__)
    def node(state: AgentState):

        tool = generator.generate(
            goal=state.goal.description,
            context=str(state.execution_result)
        )
        
        state.memory["tool_generation_attempted"] = True

        # 🔁 evitar duplicados
        if registry.exists(tool.name):
            state.memory["tool_already_exists"] = True
            return state

        if not validator.validate(tool):
            state.memory["tool_failed"] = True
            return state

        tool_instance = factory.create(tool)

        registry.register(tool_instance)

        state.memory["last_generated_tool"] = tool.name

        return state

    return node
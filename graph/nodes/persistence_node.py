from config.settings import REQUIRED_SCORE_TO_PERSIST_TOOL
from domain.models.state import AgentState
from domain.tools.registry import ToolRegistry
import logging

from utils.logging import log_block

logger = logging.getLogger(__name__)

def build_persist_tool_node(registry: ToolRegistry):

    @log_block(__name__)
    def node(state: AgentState):

        # solo si éxito
        if not state.execution_result.success:
            return state

        # solo si viene de tool generada
        tool_name = state.memory.get("last_generated_tool")

        if not tool_name:
            return state

        tool = registry.get(tool_name)

        if state.evaluation.score > REQUIRED_SCORE_TO_PERSIST_TOOL:
            registry.save(tool)
            logger.debug(f"💾 Tool '{tool_name}' persisted!")
        else:
            logger.debug(f"💾 Tool '{tool_name}' exevuted but score [{state.evaluation.score}] does not meet the required score [{REQUIRED_SCORE_TO_PERSIST_TOOL}]")

        return state

    return node
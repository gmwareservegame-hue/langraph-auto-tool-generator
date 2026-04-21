from domain.models.state import AgentState
from application.executor.executor import Executor
from utils.logging import log_block

def build_executor_node(executor: Executor):

    @log_block(__name__)
    def executor_node(state: AgentState):
        state.execution_result = executor.execute(state.plan)
        return state

    return executor_node
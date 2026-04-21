from config.settings import MAX_ITERATIONS_ALLOWED
from domain.models.state import AgentNodes, AgentState
from utils.logging import log_block


def update_iterations(state: AgentState):
    state.memory["iterations"] = state.memory.get("iterations", 0) + 1

def max_iterations_reached(state: AgentState):
    return state.memory["iterations"] > MAX_ITERATIONS_ALLOWED


@log_block(__name__)
def router_node(state: AgentState):
    
    update_iterations(state=state)
    
    if max_iterations_reached(state=state):
        raise Exception(f"Max number of iterations ({MAX_ITERATIONS_ALLOWED}) reached, the execution will stop.")

    # si necesita tool → generar
    if state.evaluation.needs_new_tool:
        return AgentNodes.GENERATE_TOOL

    # si éxito + hay tool generada → persistir
    if (
        state.evaluation.success
        and state.memory.get("last_generated_tool")
    ):
        return AgentNodes.PERSIST_TOOL

    # éxito sin tool nueva
    if state.evaluation.success:
        return "end"

    # fallback
    return AgentNodes.PLAN
from application.planner.planner import Planner
from domain.models.state import AgentState
from utils.logging import log_block

def build_planner_node(planner: Planner):

    @log_block(__name__)
    def planner_node(state: AgentState):
        state.plan = planner.create_plan(state.goal)
        return state

    return planner_node
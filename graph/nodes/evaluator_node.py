from domain.models.state import AgentState
from application.evaluator.evaluator import Evaluator
import logging

from utils.logging import log_block

logger = logging.getLogger(__name__)

def build_evaluator_node(evaluator: Evaluator):

    @log_block(__name__)
    def evaluator_node(state: AgentState):
        
        state.evaluation = evaluator.evaluate(state)
        
        return state

    return evaluator_node
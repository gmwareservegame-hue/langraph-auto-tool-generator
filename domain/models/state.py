from enum import StrEnum
from typing import Optional

from pydantic import BaseModel

from domain.models.execution_result import ExecutionResult
from domain.models.goal import Goal
from domain.models.plan import Plan
from domain.models.evaluation import Evaluation


class AgentState(BaseModel):
    goal: Goal
    plan: Optional[Plan] = None
    execution_result: Optional[ExecutionResult] = None
    evaluation: Optional[Evaluation] = None
    memory: dict = {}
    
class AgentNodes(StrEnum):
    PLAN = "plan"
    EXECUTE = "execute"
    EVALUATE = "evaluate"
    GENERATE_TOOL = "generate_tool"
    PERSIST_TOOL = "persist_tool"
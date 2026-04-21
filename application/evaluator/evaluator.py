
from domain.models.evaluation import Evaluation
from domain.models.execution_result import ExecutionResult
from domain.models.plan import Plan
from domain.models.state import AgentState
from domain.tools import registry


class Evaluator:

    def evaluate(self, state: AgentState) -> Evaluation:

        # 🔴 caso 1: tool inválida → generar
        if any(step.error == "Invalid or unknown tool" for step in state.execution_result.steps):
            return Evaluation(
                success=False,
                score=0,
                needs_new_tool=True,
                feedback="LLM could not select a valid tool"
            )

        # 🔴 caso 2: ya intentaste generar → NO repetir
        if state.memory.get("tool_generation_attempted"):
            return Evaluation(
                success=state.execution_result.success,
                score=1.0 if state.execution_result.success else 0.0,
                needs_new_tool=False,
                feedback="Tool already generated"
            )

        # 🟡 caso normal
        used_tools = len(state.plan.steps) > 0

        return Evaluation(
            success=state.execution_result.success,
            score=1.0 if state.execution_result.success else 0.0,
            needs_new_tool=not used_tools,
            feedback="No se usaron tools" if not used_tools else None
        )
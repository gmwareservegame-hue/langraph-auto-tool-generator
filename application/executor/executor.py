

from domain.models.execution_result import ExecutionResult, StepResult
from domain.models.plan import Plan
from domain.tools.registry import ToolRegistry

import logging

logger = logging.getLogger(__name__)


class Executor:
    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(self, plan: Plan) -> ExecutionResult:
        results = []

        for step in plan.steps:
            if not step.tool_name or not self.registry.exists(step.tool_name):
                results.append(StepResult(
                    tool_name=str(step.tool_name),
                    success=False,
                    error="Invalid or unknown tool"
                ))
                continue

            tool = self.registry.get(step.tool_name)

            try:
                validated_input = tool.input_model(**step.input_data)
                output = tool.run(validated_input)

                results.append(StepResult(
                    tool_name=tool.name,
                    success=True,
                    output=output.dict()
                ))

            except Exception as e:
                results.append(StepResult(
                    tool_name=tool.name,
                    success=False,
                    error=str(e)
                ))

        return ExecutionResult(
            steps=results,
            success=all(r.success for r in results)
        )

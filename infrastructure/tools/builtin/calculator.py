from domain.tools.base import Tool, ToolInput, ToolOutput
from pydantic import BaseModel


class CalculatorInput(ToolInput):
    a: float
    b: float


class CalculatorOutput(ToolOutput):
    result: float


class CalculatorTool(Tool):
    name = "calculator"
    description = "Suma dos números"
    input_model = CalculatorInput
    output_model = CalculatorOutput
    permissions = []

    def run(self, input_data: CalculatorInput) -> CalculatorOutput:
        return CalculatorOutput(result=input_data.a + input_data.b)
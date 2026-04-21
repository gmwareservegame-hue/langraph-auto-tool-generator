from domain.tools.registry import ToolRegistry

# importa tools concretas
from infrastructure.tools.builtin.calculator import CalculatorTool


def load_tools(registry: ToolRegistry):
    registry.register(CalculatorTool())
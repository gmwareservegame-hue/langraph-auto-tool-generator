from application.tool_factory.tool_factory import ToolFactory
from application.tool_generator.tool_generator import ToolGenerator
from application.tool_validator.tool_validator import ToolValidator
from domain.tools.registry import ToolRegistry
from infrastructure.tools.loader import load_tools

from application.executor.executor import Executor
from application.planner.planner import Planner
from application.evaluator.evaluator import Evaluator


def build_container():
    registry = ToolRegistry()
    load_tools(registry)

    planner = Planner(registry)
    executor = Executor(registry)
    evaluator = Evaluator()

    tool_generator = ToolGenerator()
    validator = ToolValidator()
    factory = ToolFactory()
    
    # load all existing tools
    registry.load_all(factory)

    return {
        "registry": registry,
        "planner": planner,
        "executor": executor,
        "evaluator": evaluator,
        "tool_generator": tool_generator,
        "validator": validator,
        "factory": factory
    }
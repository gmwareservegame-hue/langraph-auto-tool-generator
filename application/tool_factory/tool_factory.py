from pydantic import create_model

from domain.models.generated_tool import GeneratedTool
from domain.tools.base import Tool
from domain.tools.dynamic_tool import DynamicTool


class ToolFactory:

    def create(self, generated_tool: GeneratedTool):
        local_env = {}

        exec(generated_tool.code, {}, local_env)

        func = local_env.get("run")

        if not func:
            raise ValueError("No run() function found")

        # 🔥 crear modelo dinámico
        InputModel = create_model(
            f"{generated_tool.name}_Input",
            **{k: (object, ...) for k in generated_tool.input_schema.keys()}
        )

        OutputModel = create_model(
            f"{generated_tool.name}_Output",
            **{k: (object, ...) for k in generated_tool.output_schema.keys()}
        )

        return DynamicTool(
            name=generated_tool.name,
            description=generated_tool.description,
            func=func,
            input_model=InputModel,
            output_model=OutputModel
        )
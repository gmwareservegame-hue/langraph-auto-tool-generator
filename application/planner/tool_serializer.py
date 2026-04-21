from domain.tools.base import Tool


def serialize_tools(tools: list[Tool]) -> list[dict]:
    return [
        {
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.input_model.model_json_schema(),
        }
        for tool in tools
    ]
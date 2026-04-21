from pydantic import BaseModel


class GeneratedTool(BaseModel):
    name: str
    description: str
    input_schema: dict
    output_schema: dict
    code: str
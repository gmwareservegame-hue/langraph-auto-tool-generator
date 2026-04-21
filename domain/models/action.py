from pydantic import BaseModel
from pydantic import BaseModel, field_validator

class Action(BaseModel):
    tool_name: str
    input_data: dict
    
    @field_validator("tool_name")
    @classmethod
    def validate_tool_name(cls, v):
        if v is None or v == "null" or v.strip() == "":
            raise ValueError("tool_name cannot be null or empty")
        return v
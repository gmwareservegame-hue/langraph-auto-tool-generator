from typing import Optional

from pydantic import BaseModel


class StepResult(BaseModel):
    tool_name: str
    success: bool
    output: Optional[dict] = None
    error: Optional[str] = None


class ExecutionResult(BaseModel):
    steps: list[StepResult]
    success: bool
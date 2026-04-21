from typing import Optional

from pydantic import BaseModel


class Evaluation(BaseModel):
    success: bool
    score: float
    needs_new_tool: bool
    feedback: Optional[str] = None
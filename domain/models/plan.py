
from typing import List

from pydantic import BaseModel

from domain.models.action import Action

class Plan(BaseModel):
    steps: List[Action]
from pydantic import BaseModel
from typing import Optional, Dict, Any

class Goal(BaseModel):
    id: str
    description: str
    constraints: Optional[Dict[str, Any]] = None
    context: Optional[Dict[str, Any]] = None
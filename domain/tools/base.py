from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseModel

class ToolInput(BaseModel):
    pass

class ToolOutput(BaseModel):
    pass


class Tool(ABC):
    name: str
    description: str
    input_model: Type[ToolInput]
    output_model: Type[ToolOutput]
    permissions: list[str]

    @abstractmethod
    def run(self, input_data: ToolInput) -> ToolOutput:
        pass

from domain.tools.base import Tool


class DynamicTool(Tool):

    def __init__(self, name, description, func, input_model, output_model):
        self.name = name
        self.description = description
        self.func = func
        self.input_model = input_model
        self.output_model = output_model
        self.permissions = []

    def run(self, input_data):
        return self.func(input_data)
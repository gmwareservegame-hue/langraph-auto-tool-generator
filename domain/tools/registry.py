import json
import os
from typing import Dict, List
from application.tool_factory.tool_factory import ToolFactory
from domain.models.generated_tool import GeneratedTool
from domain.tools.base import Tool
import logging

logger = logging.getLogger(__name__)

TOOLS_PATH = "tools"


class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            logger.debug(f"[WARN] Tool '{tool.name}' already registered, skipping")
            return  # 🔥 NO lanzar excepción

        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        if name not in self._tools:
            raise ValueError(f"Tool '{name}' not found")

        return self._tools[name]

    def list(self) -> List[Tool]:
        return list(self._tools.values())

    def exists(self, name: str) -> bool:
        return name in self._tools
    
    def _write_tool(self, path, tool: Tool):
        with open(path, "w") as f:
            json.dump({
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.input_schema,
                "output_schema": tool.output_schema,
                "code": tool.code,
            }, f, indent=2)


    def _is_same_tool(self, existing: dict, tool: Tool) -> bool:
        return (
            existing.get("code") == tool.code and
            existing.get("input_schema") == tool.input_schema
        )


    def _get_next_version(self, tool_name: str) -> int:
        files = os.listdir(TOOLS_PATH)

        versions = []

        for file in files:
            if file.startswith(tool_name) and "_v" in file:
                try:
                    v = int(file.split("_v")[-1].split(".")[0])
                    versions.append(v)
                except:
                    pass

        return max(versions, default=1) + 1
        
    # 💾 GUARDAR
    def save(self, tool: Tool):

        os.makedirs(TOOLS_PATH, exist_ok=True)

        base_path = os.path.join(TOOLS_PATH, f"{tool.name}.json")

        # 🟢 CASO 1: no existe → guardar directo
        if not os.path.exists(base_path):
            self._write_tool(base_path, tool)
            logger.debug(f"💾 Tool '{tool.name}' saved")
            return

        # 🟡 CASO 2: existe → comparar
        with open(base_path) as f:
            existing = json.load(f)

        if self._is_same_tool(existing, tool):
            logger.debug(f"⚠️ Tool '{tool.name}' already exists and is identical. Skipping.")
            return

        # 🔵 CASO 3: diferente → versionar
        version = self._get_next_version(tool.name)

        versioned_path = os.path.join(
            TOOLS_PATH,
            f"{tool.name}_v{version}.json"
        )

        self._write_tool(versioned_path, tool)

        logger.debug(f"💾 Tool '{tool.name}' saved as version v{version}")

    # 📥 CARGAR
    def load_all(self, factory: ToolFactory):
        if not os.path.exists(TOOLS_PATH):
            return

        for file in os.listdir(TOOLS_PATH):
            if not file.endswith(".json"):
                continue

            path = os.path.join(TOOLS_PATH, file)

            with open(path) as f:
                data = json.load(f)

                generated = GeneratedTool(**data)
                tool = factory.create(generated)

                self.register(tool)
    
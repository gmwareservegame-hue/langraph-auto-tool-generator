class ToolValidator:

    def validate(self, tool: GeneratedTool) -> bool:

        # 🚫 ejemplo básico (luego lo mejoras)
        forbidden = ["os.", "sys.", "subprocess", "requests"]

        for word in forbidden:
            if word in tool.code:
                return False

        return True
class GeminiFlashLite_3_1_ResponseWrapper:
    def __init__(self, response):
        self._response = response

    @property
    def content(self):
        # Si content es un array, extrae los fragmentos de tipo 'text'
        if isinstance(self._response.content, list):
            texts = [item['text'] for item in self._response.content if item.get('type') == 'text']
            return "\n".join(texts)
        # Si ya es string, lo devuelve tal cual
        return self._response.content

    def __getattr__(self, name):
        # Reenvía cualquier otro atributo al objeto original
        return getattr(self._response, name)
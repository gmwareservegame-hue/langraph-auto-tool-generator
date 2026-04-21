
tool_generator_prompt_v1 ="""
Eres un generador de tools en Python.

OBJETIVO:
{goal}

CONTEXTO:
{context}

Genera una tool en Python con este formato JSON:

{{
  "name": "string",
  "description": "string",
  "input_schema": {{
    "type": "object",
    "properties": {{
      "param_name": {{
        "type": "number" | "string" | "boolean",
        "description": "descripcion del parametro"
      }}
    }},
    "required": ["param_name"]
  }},
  "output_schema": {{
    "type": "object",
    "properties": {{
      "result": {{
        "type": "number" | "string" | "boolean"
      }}
    }}
  }},
  "code": "codigo python"
}}

REGLAS IMPORTANTES:
- input_schema y output_schema deben ser JSON válidos (NO strings)
- NO pongas JSON dentro de comillas
- Cada propiedad debe tener un campo "type"
- Usa nombres claros como "celsius", "value", etc.
- La función debe llamarse run(input_data)
- input_data es un dict con los parámetros definidos
- Devuelve siempre un dict

EJEMPLO CORRECTO:

{{
  "name": "celsius_to_fahrenheit",
  "description": "Convierte Celsius a Fahrenheit",
  "input_schema": {{
    "type": "object",
    "properties": {{
      "celsius": {{
        "type": "number",
        "description": "Temperatura en grados Celsius"
      }}
    }},
    "required": ["celsius"]
  }},
  "output_schema": {{
    "type": "object",
    "properties": {{
      "fahrenheit": {{
        "type": "number"
      }}
    }}
  }},
  "code": "def run(input_data):\\n    c = input_data['celsius']\\n    return {{'fahrenheit': (c * 9/5) + 32}}"
}}

Solo devuelve JSON válido.
"""

tool_generator_prompt_v2 = """
Eres un generador de tools en Python.

OBJETIVO:
{goal}

CONTEXTO:
{context}

Genera una tool en Python con este formato JSON:

{{
  "name": "string",
  "description": "string",
  "input_schema": {{
    "type": "object",
    "properties": {{
      "param_name": {{
        "type": "number" | "string" | "boolean",
        "description": "descripcion clara del parametro"
      }}
    }},
    "required": ["param_name"]
  }},
  "output_schema": {{
    "type": "object",
    "properties": {{
      "result": {{
        "type": "number" | "string" | "boolean"
      }}
    }}
  }},
  "code": "codigo python"
}}

REGLAS IMPORTANTES:
- input_schema y output_schema deben ser JSON válidos (NO strings)
- NO pongas JSON dentro de comillas
- Cada propiedad debe tener un campo "type"
- Usa nombres de parámetros SIMPLES y DIRECTOS (ej: a, b, value, text)
- EVITA estructuras anidadas en input_schema
- EVITA arrays, objetos complejos o schemas dinámicos
- La tool debe ser FÁCIL de usar por otro sistema automático

MUY IMPORTANTE:
- Esta tool será usada por otro modelo que SOLO enviará valores concretos
- input_data SIEMPRE será un dict con valores reales (ej: {{"a": 2, "b": 3}})
- NUNCA diseñes input_schema que requiera definir "type", "properties" o "required" como input

REGLAS SOBRE EL CÓDIGO:
- La función debe llamarse run(input_data)
- input_data es un dict con los parámetros definidos
- NO valides tipos complejos, asume inputs correctos
- Devuelve siempre un dict simple
- NO uses prints, logs ni dependencias externas

EJEMPLO CORRECTO:

{{
  "name": "sum_two_numbers",
  "description": "Suma dos números",
  "input_schema": {{
    "type": "object",
    "properties": {{
      "a": {{
        "type": "number",
        "description": "Primer número"
      }},
      "b": {{
        "type": "number",
        "description": "Segundo número"
      }}
    }},
    "required": ["a", "b"]
  }},
  "output_schema": {{
    "type": "object",
    "properties": {{
      "result": {{
        "type": "number"
      }}
    }}
  }},
  "code": "def run(input_data):\\n    return {{'result': input_data['a'] + input_data['b']}}"
}}

EJEMPLO INCORRECTO (NO HACER ESTO):

{{
  "input_schema": {{
    "type": "object",
    "properties": {{
      "type": "...",
      "properties": "...",
      "required": "..."
    }}
  }}
}}

Solo devuelve JSON válido.
"""
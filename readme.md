SETUP

pip install -r requirements.txt


ARQUITECTURA

app/
│
├── main.py
├── config.py
├── database.py
├── graph.py
├── state.py
│
├── llm/
│   └── gemini.py
│
├── models/
│   ├── __init__.py
│   ├── message.py
│   ├── user_memory.py
│   ├── summary.py
│   └── episodic_memory.py
│
├── repositories/
│   ├── message_repository.py
│   ├── user_memory_repository.py
│   ├── summary_repository.py
│   └── episodic_memory_repository.py
│
├── services/
│   ├── memory_service.py
│   ├── context_builder.py
│   ├── memory_extractor_service.py
│   └── summarizer_service.py
│
└── prompts/
    └── system_prompt.py


🎯 Responsabilidad de cada capa

models/


Define tablas ORM

repositories/


Solo acceso a base de datos:

guardar
leer
actualizar
filtrar


services/

lógica de negocio:

construir memoria
decidir qué contexto cargar
combinar resumen + episodios + perfil
luego extracción automática, etc.
graph.py

Solo flujo LangGraph

llm/

Encapsula Gemini


FLUJO 

usuario escribe
   ↓
guardar human
   ↓
cargar contexto
   ↓
IA responde
   ↓
guardar AI
   ↓
extraer memoria nueva
   ↓
guardar memoria útil
   ↓
si toca → resumir bloque



1.PLAN-----2.EXECUTE----3.EVALUATE----4.END
  +                         +
-------------------3.a.GENERATE_TOOL
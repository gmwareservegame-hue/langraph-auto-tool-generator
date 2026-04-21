import os
from dotenv import load_dotenv

# Carga variables del .env
load_dotenv()

# Variables de configuración
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
LOG_FILE = os.getenv("LOG_FILE", "app.log")

REQUIRED_SCORE_TO_PERSIST_TOOL = float(os.getenv("REQUIRED_SCORE_TO_PERSIST_TOOL", 0.9))
#Max number of iterations through router node allowed to avoid AI usage issues.
MAX_ITERATIONS_ALLOWED = int(os.getenv("MAX_ITERATIONS_ALLOWED", 5))

# Validación
if not GEMINI_API_KEY:
    raise ValueError("No se encontró GEMINI_API_KEY en el archivo .env")
if not DATABASE_URL:
    raise ValueError("No se encontró DATABASE_URL en el archivo .env")
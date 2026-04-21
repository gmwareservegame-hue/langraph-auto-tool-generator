from config.settings import LOG_LEVEL, LOG_FILE
from config.logging import setup_logging
from domain.models.goal import Goal
from domain.models.state import AgentState

from app.dependencies import build_container
from graph.graph_builder import build_graph
import logging

logger = logging.getLogger(__name__)

def main():
    
    setup_logging(log_level=LOG_LEVEL, log_file=LOG_FILE)
    
    # 🔧 construir sistema
    container = build_container()
    graph = build_graph(container)
    
    # # 🎯 goal inicial
    # goal = Goal(
    #     id="1",
    #     description="Sumar dos números mayores que 0"
    # )

    goal = Goal(
        id="2",
        description="Genera codigo de prueba en python y crea una tool para ejecutarlo."
    )

    state = AgentState(goal=goal)

    # ▶️ ejecutar
    result = graph.invoke(state)

    logger.debug("\n=== RESULTADO FINAL ===")
    logger.debug(result)


if __name__ == "__main__":
    main()
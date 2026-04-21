from langgraph.graph import END, StateGraph

from graph.nodes.persistence_node import build_persist_tool_node
from domain.models.state import AgentNodes, AgentState

from graph.nodes.planner_node import build_planner_node
from graph.nodes.executor_node import build_executor_node
from graph.nodes.evaluator_node import build_evaluator_node
from graph.nodes.router_node import router_node
from graph.nodes.tool_generation_node import build_tool_generation_node


def build_graph(container):

    # 🔧 nodes con dependencias
    planner = build_planner_node(container["planner"])
    executor = build_executor_node(container["executor"])
    evaluator = build_evaluator_node(container["evaluator"])
    tool_generator_node = build_tool_generation_node(
        container["tool_generator"],
        container["validator"],
        container["factory"],
        container["registry"]
    )
    tool_persistence_node = build_persist_tool_node(container["registry"])

    graph = StateGraph(AgentState)

    # 📌 nodos
    graph.add_node(AgentNodes.PLAN, planner)
    graph.add_node(AgentNodes.EXECUTE, executor)
    graph.add_node(AgentNodes.EVALUATE, evaluator)
    graph.add_node(AgentNodes.GENERATE_TOOL, tool_generator_node)
    graph.add_node(AgentNodes.PERSIST_TOOL, tool_persistence_node)

    # 🚀 entry point
    graph.set_entry_point(AgentNodes.PLAN)

    # 🔁 flujo base
    graph.add_edge(AgentNodes.PLAN, AgentNodes.EXECUTE)
    graph.add_edge(AgentNodes.EXECUTE, AgentNodes.EVALUATE)
    

    # 🧠 routing desde evaluate (AQUÍ está la clave)
    graph.add_conditional_edges(
        AgentNodes.EVALUATE,
        router_node,
        {
            "plan": AgentNodes.PLAN,
            "generate_tool": AgentNodes.GENERATE_TOOL,
            "persist_tool": AgentNodes.PERSIST_TOOL,
            "end": END
        }
    )

    # 🔁 tool generation vuelve al plan
    graph.add_edge(AgentNodes.GENERATE_TOOL, AgentNodes.PLAN)
    graph.add_edge(AgentNodes.PERSIST_TOOL, END)

    return graph.compile()
from registry.tools import TOOLS
from agents.research_agent import build_research_agent
from agents.budget_agent import build_budget_agent
from agents.writer_agent import build_writer_agent


def build_agents():
    research = build_research_agent(tools=[TOOLS["weather_hint"]])

    budget = build_budget_agent(tools=[
        TOOLS["days_between"],
        TOOLS["estimate_budget"],
        TOOLS["fx_rate"],
    ])

    writer = build_writer_agent(tools=[])

    return {
        "research": research,
        "budget": budget,
        "writer": writer,
    }

AGENTS = build_agents()

from registry.tools import TOOLS
from agents.research_agent import research_agent
from agents.booking_agent import booking_agent
from agents.itinerary_agent import itinerary_agent
from agents.support_agent import support_agent

def build_agents():
    research = research_agent(tools=[TOOLS[""]])

    budget = booking_agent(tools=[TOOLS["days_between"], TOOLS["estimate_budget"], TOOLS["fx_rate"]])

    writer = itinerary_agent(tools=[])

    support = support_agent(tools=[])

    return {
        "research": research,
        "budget": budget,
        "writer": writer,
    }

AGENTS = build_agents()

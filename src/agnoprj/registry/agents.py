from agnoprj.registry.tools import TOOLS
from agnoprj.agents.research_agent import research_agent
from agnoprj.agents.booking_agent import booking_agent
from agnoprj.agents.itinerary_agent import itinerary_agent
from agnoprj.agents.support_agent import support_agent

def build_agents():
    research = research_agent(tools=[TOOLS["duckduckgo"], TOOLS["openweather"]])

    booking = booking_agent(tools=[TOOLS["search_flights_amadeus"],TOOLS["brightdata"],TOOLS["apify_google_places"],TOOLS["duckduckgo"]])

    itinerary = itinerary_agent(tools=[TOOLS["google_maps"], TOOLS["duckduckgo"]])

    support = support_agent(tools=[TOOLS["duckduckgo"]])

    return {
        "research": research,
        "booking": booking,
        "itinerary": itinerary,
        "support": support,
    }

AGENTS = build_agents()

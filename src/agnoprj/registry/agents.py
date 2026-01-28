from registry.tools import TOOLS
from agents.research_agent import research_agent
from agents.booking_agent import booking_agent
from agents.itinerary_agent import itinerary_agent
from agents.support_agent import support_agent

def build_agents():
    research = research_agent(tools=[TOOLS["DuckDuckGoTools"], TOOLS["OpenWeatherTools"]])

    booking = booking_agent(tools=[TOOLS["search_flights_amadeus"], TOOLS["BrightDataTools"], TOOLS["ApifyTools"], TOOLS["DuckDuckGoTools"]])

    itinerary = itinerary_agent(tools=[TOOLS["GoogleMapTools"], TOOLS["DuckDuckGoTools"]])

    support = support_agent(tools=[])

    return {
        "research": research,
        "booking": booking,
        "itinerary": itinerary,
        "support": support,
    }

AGENTS = build_agents()

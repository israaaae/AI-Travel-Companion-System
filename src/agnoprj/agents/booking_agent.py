from __future__ import annotations

from typing import Any, Sequence
from agnoprj.core import BaseAgent
from agnoprj.tools.search_flights_amadeus import search_flights_amadeus
from agno.tools.brightdata import BrightDataTools
from agno.tools.apify import ApifyTools
from agno.tools.duckduckgo import DuckDuckGoTools
from datetime import datetime

def booking_agent(*, tools: Sequence[Any]):
    return BaseAgent(
        name="Booking Agent",
        tools=tools if tools is not None else [
            search_flights_amadeus,  # Your Amadeus tool ✅
            BrightDataTools(web_data_feed=True),  # Hotels
            ApifyTools(actors=["compass/crawler-google-places"]),  # Restaurants
            DuckDuckGoTools(),  # General search
        ],
        instructions=[
            f"You're a booking assistant. Today is {datetime.now()}.",
            "Use search_flights_amadeus for flight searches",
            "Use BrightData for hotel bookings",
            "Use ApifyTools for restaurant searches",
        ],
        show_tool_calls=True,
        markdown=True,
    ).build()

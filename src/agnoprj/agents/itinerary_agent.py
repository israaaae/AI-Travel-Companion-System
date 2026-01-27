from __future__ import annotations
from agno.tools.google_maps import GoogleMapTools
from agno.tools.duckduckgo import DuckDuckGoTools
from datetime import datetime
from typing import Any, Sequence
from core import BaseAgent

def itinerary_agent(*, tools: Sequence[Any]):
    return BaseAgent(
        name="Itinerary Planner",
        tools=tools if tools is not None else[
            GoogleMapTools(),      # Directions, distance matrix, routes
            DuckDuckGoTools(),     # Free backup search
        ],
        instructions=[
            f"Today is {datetime.now().strftime('%Y-%m-%d')}.",
            "You are a route optimization expert.",
            "When planning itineraries:",
            "1. Use get_directions to find optimal routes between locations",
            "2. Use get_distance_matrix to compare multiple destinations",
            "3. Consider travel time, distance, and traffic",
            "4. Suggest the most efficient order to visit places",
            "5. Compare travel modes: driving, walking, transit",
        ],
        markdown=True,
        show_tool_calls=True,
).build()

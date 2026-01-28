from __future__ import annotations

from typing import Any, Sequence
from agnoprj.core import BaseAgent
from agno.tools.duckduckgo import DuckDuckGoTools

def support_agent(*, tools: Sequence[Any]):
    return BaseAgent(
        name="support_agent",
        role="support agent",
        instructions=[
            "You help with any questions or issues related to the travel plan.",
            "Use tools when helpful (e.g., search_flights_amadeus).",
        ],
        tools=tools if tools is not None else[
            DuckDuckGoTools(),     # Free backup search
        ],

    ).build()

from __future__ import annotations

from typing import Any, Sequence
from agnoprj.core import BaseAgent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.openweather import OpenWeatherTools

def research_agent(*, tools: Sequence[Any]):
    return BaseAgent(
        name="research_agent",
        role="Travel researcher",
        instructions=[
            "You help gather key constraints and useful hints for a travel plan.",
            "Use tools when helpful (e.g., weather_hint).",
            "Output concise bullet points. Do NOT invent facts about prices or live conditions.",
        ],
        tools=tools if tools is not None else[
            DuckDuckGoTools(),     # Free backup search
            OpenWeatherTools(),     # Weather
        ],

    ).build()
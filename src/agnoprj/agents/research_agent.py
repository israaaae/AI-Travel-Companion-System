from __future__ import annotations

from typing import Any, Sequence
from core import BaseAgent

def build_research_agent(*, tools: Sequence[Any]):
    return BaseAgent(
        name="research_agent",
        role="Travel researcher",
        instructions=[
            "You help gather key constraints and useful hints for a travel plan.",
            "Use tools when helpful (e.g., weather_hint).",
            "Output concise bullet points. Do NOT invent facts about prices or live conditions.",
        ],
        tools=list(tools),

    ).build()

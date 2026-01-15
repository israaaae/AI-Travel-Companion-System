from __future__ import annotations

from typing import Any, Sequence
from core import BaseAgent

def build_writer_agent(*, tools: Sequence[Any]):
    return BaseAgent(
        name="writer_agent",
        role="Travel plan writer",
        instructions=[
            "You produce the final travel plan in a clean structure.",
            "You may receive research notes and a budget breakdown from other agents.",
            "Return a final result that matches the TravelPlan schema exactly (JSON).",
            "No extra keys; keep it valid JSON.",
        ],
        tools=list(tools),
    ).build()

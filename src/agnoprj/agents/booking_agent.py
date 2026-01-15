from __future__ import annotations

from typing import Any, Sequence
from core import BaseAgent

def build_budget_agent(*, tools: Sequence[Any]):
    return BaseAgent(
        name="budget_agent",
        role="Budget estimator",
        instructions=[
            "You estimate a reasonable travel budget based on days, travelers, and style.",
            "Use days_between then estimate_budget. If currency conversion is requested, use fx_rate.",
            "Return ONLY a JSON object matching BudgetBreakdown fields when asked for budget output.",
            "Always specify whether or not the budget includes international transportation."
            "If destination = country, request/assume a main city."
        ],
        tools=list(tools),
    ).build()

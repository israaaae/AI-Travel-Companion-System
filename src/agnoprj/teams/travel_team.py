from __future__ import annotations

from typing import Any, Sequence
from agno.models.openai import OpenAIChat
from agnoprj.core import BaseTeam
from agnoprj.core.config import SETTINGS

def _team_model():
    # même logique que tes agents
    if SETTINGS.DEFAULT_MODEL_PROVIDER == "openai":
        from agno.models.openai import OpenAIChat
        return OpenAIChat(id=SETTINGS.DEFAULT_MODEL_ID)
    if SETTINGS.DEFAULT_MODEL_PROVIDER == "google":
        from agno.models.google import Gemini  # type: ignore
        return Gemini(id=SETTINGS.DEFAULT_MODEL_ID)
    return None


def build_travel_team(*, members):
    return BaseTeam(
        name="travel_team",
        role="Travel team (research + booking + itinerary + support)",
        model=_team_model(),  # ✅ COMME DANS LA DOC: Team a un model

        members=list(members),
        instructions=[
            "You are an orchestrator. You MUST delegate tasks to members.",
            "The user input is a JSON string matching TravelRequest.",
            "When calling delegate_task_to_member, ALWAYS pass the EXACT same JSON string as the member input.",
            "Never send empty input. Never paraphrase. Do not wrap in markdown.",
            "1) Delegate to research_agent with the original JSON string.",
            "2) Delegate to booking_agent with the original JSON string.",
            "Return a short combined summary for the next step.",
        ],
        extra={"show_members_responses": True,
              "determine_input_for_members": False,
                }
    ).build()


# Backward-compatible alias (older code may call travel_team())
travel_team = build_travel_team

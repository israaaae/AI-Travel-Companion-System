from agnoprj.registry.agents import AGENTS
from agnoprj.teams.travel_team import build_travel_team

def build_teams():
    travel_team = build_travel_team(members=[AGENTS["research"], AGENTS["booking"], AGENTS["itinerary"], AGENTS["support"]])
    return {"travel": travel_team}

TEAMS = build_teams()
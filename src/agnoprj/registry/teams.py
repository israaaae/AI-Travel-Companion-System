from registry.agents import AGENTS
from teams.travel_team import build_travel_team

def build_teams():
    travel_team = build_travel_team(members=[AGENTS["research"], AGENTS["budget"]])
    return {"travel": travel_team}

TEAMS = build_teams()
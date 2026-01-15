from registry.agents import AGENTS
from teams.planning_team import build_planning_team

def build_teams():
    planning_team = build_planning_team(members=[AGENTS["research"], AGENTS["budget"]])
    return {"planning": planning_team}

TEAMS = build_teams()
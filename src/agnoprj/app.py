from dotenv import load_dotenv

load_dotenv()

from core import AgentOSFactory
from registry import AGENTS, TEAMS, WORKFLOWS
from utils.logging import LOGGER

LOGGER.info("Starting AgentOS...")

agent_os = AgentOSFactory(
    agents=list(AGENTS.values()),
    teams=list(TEAMS.values()),
).build()

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="app:app", reload=True)

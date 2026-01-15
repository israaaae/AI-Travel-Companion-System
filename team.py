from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

db = SqliteDb(db_file="tmp/team.db")

# Member Agents - Add: tools, role, name, id
agent1 = Agent(
    id="research-agent",
    name="Research Agent",
    role="Research topics and gather information",
    tools=[DuckDuckGoTools()],
    # NO memory/history params here
)

agent2 = Agent(
    id="fact-checker",
    name="Fact Checker",
    role="Verify facts and flag confidence",
    tools=[...],
)

agent3 = Agent(
    id="summarizer",
    name="Summarizer",
    role="Write final briefings",
)

agent4 = Agent(
    id="editor",
    name="Editor",
    role="Review and polish content",
)

# Team Leader - Add: memory, history, db, UI params
team = Team(
    name="Newsroom Team",
    members=[agent1, agent2, agent3, agent4],
    model=OpenAIChat(id="gpt-4o"),
    db=db,  # ← Required for persistence
    
    # History (Team level)
    add_history_to_context=True,
    num_history_runs=5,
    add_team_history_to_members=True,
    share_member_interactions=True,
    
    # Memory (Team level)
    enable_user_memories=True,
    add_memories_to_context=True,
    enable_session_summaries=True,
    
    # UI/Formatting (Team level)
    markdown=True,
    add_datetime_to_context=True,  #ki3ref chno howa la date dyal lyom, ghan7tajo f weather
    
    # Coordination
    instructions=["Coordinate members to research, verify, summarize, and edit."],
)

# Always pass user_id when running
 team.run("Your question", user_id="user_123")
# AgnoPrj (Agno AgentOS + Travel Team)

This repository contains:

- **Backend (Python)**: an [Agno](https://pypi.org/project/agno/) **AgentOS** (FastAPI) that exposes your agents/teams over HTTP.
- **Frontend (optional)**: `agent-ui/` (Next.js) – a modern chat UI that can connect to the AgentOS server.

## Quick start (backend)

### 1) Install dependencies (Poetry)

```bash
poetry install
```

### 2) Create your `.env`

Create a file named `.env` in the project root (same folder as `pyproject.toml`).

Common env vars you may want:

- **OpenAI**
  - `OPENAI_API_KEY=...`
- **Amadeus (flight search tool)**
  - `AMADEUS_CLIENT_ID=...`
  - `AMADEUS_CLIENT_SECRET=...`
- **Optional**
  - `SQLITE_DB_FILE=data/agents.db` (defaults to this)
  - `DEFAULT_MODEL_PROVIDER=openai`
  - `DEFAULT_MODEL_ID=gpt-4o-mini`

### 3) Run the AgentOS server

```bash
poetry run python -m agnoprj.app
```

By default this serves on:

- **http://127.0.0.1:2222**

> Note: the port is defined in `AgentOSFactory.serve(...)` (`src/agnoprj/core/base_orchestrator.py`).

## Optional: run the UI (agent-ui)

If you want the UI locally:

```bash
cd agent-ui
pnpm install
pnpm dev
```

The UI runs on:

- **http://localhost:3000**

And it can connect to your AgentOS instance (by default you’ll point it at `http://localhost:2222` for this project).

## Project structure

```text
src/agnoprj/
  app.py                 # AgentOS FastAPI entrypoint
  core/                  # Base wrappers/builders (BaseAgent, BaseTeam, AgentOSFactory, config)
  registry/              # Where agents/teams/tools are wired together
  agents/                # Individual agent definitions
  teams/                 # Team orchestrators (multi-agent coordination)
  tools/                 # Custom tools (e.g., Amadeus flight search)
  utils/                 # Logging, validation, paths, helpers
agent-ui/                # Optional Next.js chat UI
```

## What’s included

### Agents

Agents are built in `src/agnoprj/registry/agents.py`:

- `research`: travel research + weather/search tools
- `booking`: flights/hotels/places search tools (Amadeus + BrightData + Apify + DuckDuckGo)
- `itinerary`: route planning (Google Maps) + search
- `support`: general help

### Team

Teams are built in `src/agnoprj/registry/teams.py`:

- `travel`: orchestrates the travel workflow by delegating to member agents

## Notes

- **Persistence**: Agents use SQLite by default (`data/agents.db`). Configure via `SQLITE_DB_FILE`.
- **Logs**: written under `logs/` (see `src/agnoprj/utils/logging.py`).
- **Git**: `agent-ui/` is currently ignored via `.gitignore`. Remove that ignore rule if you want to commit/deploy the UI from this repo.
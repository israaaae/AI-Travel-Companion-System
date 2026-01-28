# AgnoPrj (AI Travel Assistant)

## What this project does (non‑technical)

This project is an **AI travel assistant** made of multiple “specialists” that work together.

When you ask a travel question (for example: *“Plan me a 5‑day trip to Paris with a $1200 budget”*), the system can:

- **Research**: find helpful information and constraints (best areas, must‑see places, weather hints).
- **Plan the itinerary**: propose a day‑by‑day plan and a good order to visit places.
- **Help with bookings**: search flights and suggest hotels/places to consider.
- **Support**: answer follow‑up questions and refine the plan.

Think of it like a small travel agency team, but automated: one AI focuses on research, another on bookings, another on routing/itinerary, and a “team lead” combines everything into one clear result.

## For developers (technical overview)

This repository contains:

- **Backend (Python)**: an [Agno](https://pypi.org/project/agno/) AgentOS server that exposes your agents/teams over HTTP.
- **Frontend (optional)**: `agent-ui/` (Next.js) – a chat UI that can connect to the server.

How it’s wired:

- **Server entry point**: `src/agnoprj/app.py`
- **Tools registry**: `src/agnoprj/registry/tools.py`
- **Agents registry**: `src/agnoprj/registry/agents.py`
- **Teams registry**: `src/agnoprj/registry/teams.py` (the `travel` team coordinates the agents)

## Quick start (backend)

### 1) Install dependencies (Poetry)

```bash
poetry install
```
### 2) Run the AgentOS server

```bash
poetry run python -m agnoprj.app
```
By default this serves on:
- **http://127.0.0.1:2222**


### 3) Optional: run the UI (agent-ui)

If you want the UI locally:

```bash
cd agent-ui
npm install
npm dev
```
The UI runs on:
- **http://localhost:3000**


## Project structure

```text
src/agnoprj/
  app.py                  # Starts the API server (AgentOS)
  registry/
    tools.py              # Tool definitions (search/weather/maps/Amadeus/etc.)
    agents.py             # Builds agents and assigns tools to them
    teams.py              # Builds teams (the "travel" team)
  agents/                 # The individual AI specialists (research/booking/itinerary/support)
  teams/                  # The team “manager” that coordinates specialists
  tools/                  # Custom tools (e.g., `search_flights_amadeus.py`)
  core/                   # Shared builders/config (BaseAgent/BaseTeam, settings, DB, errors)
  utils/                  # Logging + small helpers

data/                     # Local SQLite DB files (created at runtime)
logs/                     # Runtime logs (created at runtime)

agent-ui/                 # Next.js chat UI 
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
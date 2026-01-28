from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Sequence
from agno.os import AgentOS
from agnoprj.core.config import SETTINGS
from agnoprj.core.exceptions import OrchestratorError


@dataclass
class AgentOSFactory:
    """AgentOS builder (FastAPI runtime)."""

    agents: Sequence[Any] = field(default_factory=list)
    teams: Sequence[Any] = field(default_factory=list)
    workflows: Sequence[Any] = field(default_factory=list)
    description: str = SETTINGS.AGENT_OS_DESCRIPTION
    extra: dict = field(default_factory=dict)

    def build(self) -> AgentOS:
        try:
            kwargs = dict(
                description=self.description,
                agents=list(self.agents) if self.agents else None,
                teams=list(self.teams) if self.teams else None,
                workflows=list(self.workflows) if self.workflows else None,
            )
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            kwargs.update(self.extra)
            return AgentOS(**kwargs)
        except Exception as e:
            raise OrchestratorError(f"Failed to build AgentOS: {e}") from e

    def get_app(self):
        return self.build().get_app()

    def serve(self, app: str, reload: bool = False, host: str = "127.0.0.1", port: int = 2222):
        return self.build().serve(app=app, reload=reload, host=host, port=port)

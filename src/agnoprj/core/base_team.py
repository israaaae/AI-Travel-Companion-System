from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List, Optional, Sequence
from agno.team import Team
from agnoprj.core.exceptions import TeamBuildError

@dataclass
class BaseTeam:
    name: str
    role: Optional[str] = None
    model: Any = None 
    members: Sequence[Any] = field(default_factory=list)
    instructions: Optional[str | List[str]] = None
    tools: Optional[list[Any]] = None
    extra: dict = field(default_factory=dict)

    def build(self) -> Team:
        try:
            kwargs = dict(
                name=self.name,
                role=self.role,
                model=self.model,          
                members=list(self.members),
                instructions=self.instructions,
                tools=self.tools,
            )
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            kwargs.update(self.extra)
            return Team(**kwargs)
        except Exception as e:
            raise TeamBuildError(f"Failed to build Team {self.name!r}: {e}") from e

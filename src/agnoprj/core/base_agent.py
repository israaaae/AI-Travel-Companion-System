from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Optional, Sequence

from agno.agent import Agent
from core.config import SETTINGS
from core.db import get_sqlite_db
from core.exceptions import AgentBuildError


def _default_model():
    provider = SETTINGS.DEFAULT_MODEL_PROVIDER
    model_id = SETTINGS.DEFAULT_MODEL_ID

    if provider == "openai":
        from agno.models.openai import OpenAIChat
        return OpenAIChat(id=model_id)

    if provider == "google":
        from agno.models.google import Gemini  # type: ignore
        return Gemini(id=model_id)

    raise AgentBuildError(
        f"Unsupported DEFAULT_MODEL_PROVIDER={provider!r}. "
        "Use openai|anthropic|google or pass an explicit model instance."
    )


@dataclass
class BaseAgent:
    """Stable Agno Agent wrapper (builder)."""

    name: str
    role: Optional[str] = None
    instructions: Optional[str | list[str]] = None
    model: Any = None
    tools: Sequence[Callable[..., Any] | Any] = field(default_factory=list)

    db_enabled: bool = True
    add_history_to_context: bool = SETTINGS.ADD_HISTORY_TO_CONTEXT
    markdown: bool = SETTINGS.MARKDOWN
    input_schema: Any = None
    output_schema: Any = None
    extra: dict = field(default_factory=dict)

    def build(self) -> Agent:
        try:
            model = self.model or _default_model()
            db = get_sqlite_db() if self.db_enabled else None

            kwargs = dict(
                name=self.name,
                model=model,
                tools=list(self.tools) if self.tools else None,
                role=self.role,
                instructions=self.instructions,
                db=db,
                add_history_to_context=self.add_history_to_context,
                markdown=self.markdown,
            )

            if self.input_schema is not None:
                kwargs["input_schema"] = self.input_schema
            if self.output_schema is not None:
                kwargs["output_schema"] = self.output_schema

            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            kwargs.update(self.extra)

            return Agent(**kwargs)
        except Exception as e:
            raise AgentBuildError(f"Failed to build Agent {self.name!r}: {e}") from e

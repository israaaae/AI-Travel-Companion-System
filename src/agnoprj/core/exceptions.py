from __future__ import annotations 
# achno ki3ni had __future__


class CoreError(Exception):
    """Base error for the framework."""


class ConfigError(CoreError):
    """Raised when configuration is missing or invalid."""


class ValidationError(CoreError):
    """Raised when input/output validation fails."""


class ToolError(CoreError):
    """Raised when a tool fails."""


class AgentBuildError(CoreError):
    """Raised when an Agent cannot be constructed."""


class TeamBuildError(CoreError):
    """Raised when a Team cannot be constructed."""


class OrchestratorError(CoreError):
    """Raised for AgentOS/runtime orchestration issues."""

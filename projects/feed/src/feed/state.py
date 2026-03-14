"""Track pipeline state for idempotent runs."""

import json
import logging
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class PipelineState:
    """Persistent state between runs."""
    last_run: str | None = None
    processed_message_ids: list[str] = field(default_factory=list)
    total_issues_generated: int = 0


def load_state(state_path: Path) -> PipelineState:
    """Load state from disk, or return fresh state."""
    if not state_path.exists():
        logger.info("No state file found — starting fresh")
        return PipelineState()

    try:
        with open(state_path) as f:
            data = json.load(f)
        state = PipelineState(
            last_run=data.get("last_run"),
            processed_message_ids=data.get("processed_message_ids", []),
            total_issues_generated=data.get("total_issues_generated", 0),
        )
        logger.info(
            "Loaded state: last_run=%s, %d processed messages",
            state.last_run, len(state.processed_message_ids),
        )
        return state
    except (json.JSONDecodeError, KeyError):
        logger.warning("Corrupt state file — starting fresh")
        return PipelineState()


def save_state(state: PipelineState, state_path: Path) -> None:
    """Persist state to disk."""
    state_path.parent.mkdir(parents=True, exist_ok=True)
    with open(state_path, "w") as f:
        json.dump(asdict(state), f, indent=2)
    logger.debug("State saved to %s", state_path)


def get_last_run_datetime(state: PipelineState) -> datetime | None:
    """Parse last_run timestamp, or None if never run."""
    if not state.last_run:
        return None
    try:
        return datetime.fromisoformat(state.last_run)
    except ValueError:
        return None

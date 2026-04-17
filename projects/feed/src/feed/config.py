"""Load and validate Feed configuration."""

from dataclasses import dataclass, field
from pathlib import Path
import yaml


CONFIG_DIR = Path.home() / ".config" / "feed"
DEFAULT_CONFIG_PATH = CONFIG_DIR / "config.yaml"


@dataclass
class GmailConfig:
    label: str = "FOOD"
    max_emails_per_run: int = 20


@dataclass
class RemarkableConfig:
    folder: str = "/Feed"


@dataclass
class MagazineConfig:
    max_articles: int = 15
    max_links_per_email: int = 3
    output_dir: str = "~/feed-output"

    @property
    def output_path(self) -> Path:
        return Path(self.output_dir).expanduser()


@dataclass
class Config:
    gmail: GmailConfig = field(default_factory=GmailConfig)
    remarkable: RemarkableConfig = field(default_factory=RemarkableConfig)
    magazine: MagazineConfig = field(default_factory=MagazineConfig)
    log_level: str = "info"
    credentials_path: Path = field(default_factory=lambda: CONFIG_DIR / "credentials.json")
    token_path: Path = field(default_factory=lambda: CONFIG_DIR / "token.json")
    state_path: Path = field(default_factory=lambda: CONFIG_DIR / "state.json")


def load_config(path: Path | None = None) -> Config:
    """Load config from YAML file, validate required fields."""
    config_path = path or DEFAULT_CONFIG_PATH

    if not config_path.exists():
        raise FileNotFoundError(
            f"Config file not found at {config_path}\n"
            f"Copy config.example.yaml to {config_path} and fill in your values."
        )

    with open(config_path) as f:
        raw = yaml.safe_load(f) or {}

    config = Config()

    gmail_raw = raw.get("gmail", {})
    config.gmail = GmailConfig(
        label=gmail_raw.get("label", "FOOD"),
        max_emails_per_run=gmail_raw.get("max_emails_per_run", 20),
    )

    rm_raw = raw.get("remarkable", {})
    config.remarkable = RemarkableConfig(
        folder=rm_raw.get("folder", "/Feed"),
    )

    mag_raw = raw.get("magazine", {})
    config.magazine = MagazineConfig(
        max_articles=mag_raw.get("max_articles", 15),
        max_links_per_email=mag_raw.get("max_links_per_email", 3),
        output_dir=mag_raw.get("output_dir", "~/feed-output"),
    )

    config.log_level = raw.get("logging", {}).get("level", "info")

    _validate(config)
    return config


def _validate(config: Config) -> None:
    """Check required fields are present."""
    errors = []

    if not config.gmail.label:
        errors.append("gmail.label is required")

    if errors:
        raise ValueError("Config validation failed:\n  - " + "\n  - ".join(errors))

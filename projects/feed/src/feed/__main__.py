"""Feed CLI entry point."""

import argparse
import logging
import sys
from pathlib import Path

from feed.config import load_config, CONFIG_DIR


def setup_logging(level: str) -> None:
    """Configure structured logging."""
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def cmd_setup(config) -> None:
    """Run OAuth2 flow to authenticate with Gmail."""
    from feed.gmail import authenticate

    print("Starting Gmail OAuth2 setup...")
    print(f"  Credentials: {config.credentials_path}")
    print(f"  Token will be saved to: {config.token_path}")
    print()

    authenticate(config.credentials_path, config.token_path)
    print("\nSetup complete. You can now run 'feed' or 'feed --dry-run'.")


def cmd_dry_run(config) -> None:
    """Scan Gmail, extract content, generate PDF locally — don't send."""
    from feed.pipeline import run_pipeline

    run_pipeline(config, dry_run=True)


def cmd_run(config) -> None:
    """Full pipeline: scan → extract → PDF → send to reMarkable."""
    from feed.pipeline import run_pipeline

    run_pipeline(config, dry_run=False)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="feed",
        description="Scan Gmail for food content, build a magazine PDF, send to reMarkable.",
    )
    parser.add_argument(
        "--setup",
        action="store_true",
        help="Run OAuth2 setup (first time only)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Scan and generate PDF locally without sending",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help=f"Path to config file (default: {CONFIG_DIR / 'config.yaml'})",
    )
    parser.add_argument(
        "--log-level",
        default=None,
        choices=["debug", "info", "warning", "error"],
        help="Override log level from config",
    )

    args = parser.parse_args()

    # Setup mode only needs credentials path, not full config validation
    if args.setup:
        config_path = args.config
        try:
            config = load_config(config_path)
        except (FileNotFoundError, ValueError):
            # Minimal config for setup — just need credential paths
            from feed.config import Config
            config = Config()

        setup_logging(args.log_level or "info")
        cmd_setup(config)
        return

    try:
        config = load_config(args.config)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    setup_logging(args.log_level or config.log_level)

    if args.dry_run:
        cmd_dry_run(config)
    else:
        cmd_run(config)


if __name__ == "__main__":
    main()

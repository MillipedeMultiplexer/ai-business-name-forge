"""Typer CLI entrypoint for the forge tool."""

from __future__ import annotations

import logging
import sys

import typer
from rich.console import Console

from forge_app.bootstrap import build_container
from forge_handlers.generate_handler import GenerateHandler
from forge_handlers.batch_handler import BatchHandler

app = typer.Typer(
    name="forge",
    help="AI business name generator — forge names that don't suck.",
    no_args_is_help=True,
)
console = Console()


def _init_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.WARNING,
        format="%(asctime)s %(levelname)s %(name)s :: %(message)s",
    )


@app.command()
def generate(
    brief: str = typer.Argument(..., help="One-line description of the business."),
    count: int = typer.Option(12, "--count", "-n", min=1, max=200),
    style: str = typer.Option("modern", "--style", "-s"),
    tld: str = typer.Option("com", "--tld"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Generate business names from a brief."""
    _init_logging(verbose)
    container = build_container()
    handler = GenerateHandler(container=container, console=console)
    handler.run(brief=brief, count=count, style=style, tld=tld)


@app.command()
def batch(
    briefs_file: str = typer.Argument(..., help="Path to newline-delimited briefs."),
    out: str = typer.Option("out/names.csv", "--out", "-o"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Batch-generate names from a file of briefs."""
    _init_logging(verbose)
    container = build_container()
    handler = BatchHandler(container=container, console=console)
    handler.run(briefs_path=briefs_file, out_path=out)


def main() -> None:
    try:
        app()
    except KeyboardInterrupt:
        console.print("[yellow]interrupted[/yellow]")
        sys.exit(130)


if __name__ == "__main__":
    main()
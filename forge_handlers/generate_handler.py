"""GenerateHandler: CLI-facing adapter for one generation request."""

from __future__ import annotations

from dataclasses import dataclass

from rich.console import Console
from rich.table import Table

from forge_app.bootstrap import Container
from forge_models.generation_request import GenerationRequest


@dataclass(slots=True)
class GenerateHandler:
    """Renders generate results. No business logic lives here."""

    container: Container
    console: Console

    def run(self, *, brief: str, count: int, style: str, tld: str) -> None:
        request = GenerationRequest(brief=brief, count=count, style=style, tld=tld)
        results = self.container.generation.generate(request)

        if not results:
            self.console.print("[red]no names survived screening[/red]")
            return

        table = Table(title=f"forged names — {brief}", show_lines=False)
        table.add_column("#", justify="right", style="dim")
        table.add_column("name", style="bold")
        table.add_column(f".{tld}", style="cyan")
        table.add_column("score", justify="right", style="green")

        for i, scored in enumerate(results, start=1):
            table.add_row(
                str(i),
                scored.candidate.display,
                scored.candidate.slug,
                f"{scored.brandability:.2f}",
            )
        self.console.print(table)
"""BatchHandler: reads briefs from a file, writes CSV output."""

from __future__ import annotations

import csv
import logging
from dataclasses import dataclass
from pathlib import Path

from rich.console import Console
from rich.progress import track

from forge_app.bootstrap import Container
from forge_models.generation_request import GenerationRequest

log = logging.getLogger("forge.handlers.batch")


@dataclass(slots=True)
class BatchHandler:
    """Batch generation driver. Streams output; never buffers all rows."""

    container: Container
    console: Console

    def run(self, *, briefs_path: str, out_path: str) -> None:
        briefs = [line.strip() for line in Path(briefs_path).read_text("utf-8").splitlines()]
        briefs = [b for b in briefs if b and not b.startswith("#")]

        out = Path(out_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        with out.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["brief", "rank", "name", "slug", "tld", "score"])
            for brief in track(briefs, description="forging"):
                req = GenerationRequest(brief=brief, count=10, style="modern", tld="com")
                for rank, scored in enumerate(self.container.generation.generate(req), start=1):
                    writer.writerow([
                        brief,
                        rank,
                        scored.candidate.display,
                        scored.candidate.slug,
                        scored.candidate.tld,
                        f"{scored.brandability:.2f}",
                    ])
        self.console.print(f"[green]wrote {out}[/green]")
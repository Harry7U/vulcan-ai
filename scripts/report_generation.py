import json
from pathlib import Path
from rich.console import Console

OUTPUT_DIR = Path("output")

def generate_reports():
    console = Console()
    console.print("[title]📊 Generating reports in JSON, CSV, and custom formats...[/title]")
    reports_dir = OUTPUT_DIR / "
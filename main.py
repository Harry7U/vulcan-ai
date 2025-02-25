#!/usr/bin/env python3
"""
Vulcan - Hunter's Arsenal
An advanced, modular, AI-driven bug bounty hunting tool with colorful animations and real-time feedback.

Usage:
    python main.py --all
    python main.py --recon
    python main.py --fuzz
    python main.py --exploit
    python main.py --generate
    python main.py --report
    python main.py --feedback
"""

import argparse
import json
import threading
import subprocess
import time
from pathlib import Path
import openai

# Import libraries for colorful output and animations
from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

# Import custom modules
import subdomain_enumeration
import url_collection
import vulnerability_filtering
import ai_payload_generation
import vulnerability_testing
import ai_fuzzing
import report_generation

# Define a custom theme for Rich
custom_theme = Theme({
    "info": "bold cyan",
    "success": "bold green",
    "warning": "bold yellow",
    "error": "bold red",
    "title": "bold magenta"
})
console = Console(theme=custom_theme)

# Define paths
CONFIG_FILE = Path("config/config.json")
OUTPUT_DIR = Path("output")

def load_config():
    if not CONFIG_FILE.exists():
        console.print(f"[error]⚠️ Configuration file {CONFIG_FILE} not found.[/error]")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

config = load_config()
openai.api_key = config['openai_api_key']

def run_all():
    console.print(Panel("[title]🔥 Starting Full Workflow: Recon → Fuzz → Exploit → Generate → Report[/title]", expand=False))
    tasks = [
        subdomain_enumeration.enumerate_subdomains,
        url_collection.collect_urls,
        vulnerability_filtering.categorize_urls,
        ai_payload_generation.generate_payloads,
        vulnerability_testing.run_tests,
        ai_fuzzing.fuzz_parameters,
        report_generation.generate_reports
    ]
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task1 = progress.add_task("[cyan]Running subdomain enumeration...", total=100)
        task2 = progress.add_task("[magenta]Running URL collection...", total=100)
        task3 = progress.add_task("[yellow]Categorizing URLs...", total=100)
        task4 = progress.add_task("[green]Generating payloads...", total=100)
        task5 = progress.add_task("[blue]Running vulnerability tests...", total=100)
        task6 = progress.add_task("[cyan]Fuzzing parameters...", total=100)
        task7 = progress.add_task("[green]Generating reports...", total=100)
        
        threads = []
        for task in tasks:
            t = threading.Thread(target=task)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
            progress.update(task1, advance=20)
            progress.update(task2, advance=20)
            progress.update(task3, advance=20)
            progress.update(task4, advance=20)
            progress.update(task5, advance=20)
            progress.update(task6, advance=20)
            progress.update(task7, advance=20)
    
    console.print("[success]All tasks have finished successfully! 🚀[/success]")

def main():
    parser = argparse.ArgumentParser(description="Vulcan - Advanced Bug Bounty Tool")
    parser.add_argument("--recon", "-r", action="store_true", help="Run all reconnaissance modules")
    parser.add_argument("--fuzz", "-f", action="store_true", help="Run fuzzing modules")
    parser.add_argument("--exploit", "-e", action="store_true", help="Run exploitation modules")
    parser.add_argument("--generate", "-g", action="store_true", help="Generate AI-based payloads")
    parser.add_argument("--report", "-rp", action="store_true", help="Generate reports")
    parser.add_argument("--feedback", "-fb", action="store_true", help="Collect and store user feedback")
    parser.add_argument("--all", "-a", action="store_true", help="Run the complete workflow: recon → fuzz → exploit → generate → report")
    
    args = parser.parse_args()

    if args.all:
        run_all()
    else:
        if args.recon:
            subdomain_enumeration.enumerate_subdomains("example.com")
        if args.fuzz:
            ai_fuzzing.fuzz_parameters()
        if args.exploit:
            vulnerability_testing.run_tests()
        if args.generate:
            ai_payload_generation.generate_payloads("xss")
        if args.report:
            report_generation.generate_reports()
        if args.feedback:
            console.print("[info]Collecting feedback is not implemented yet.[/info]")
        if len(vars(args)) == 1:
            parser.print_help()

if __name__ == "__main__":
    main()
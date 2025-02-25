import subprocess
from pathlib import Path
from rich.console import Console
from rich.progress import Progress

OUTPUT_DIR = Path("output")

def enumerate_subdomains(domain):
    console = Console()
    console.print("[title]🚀 Running subdomain enumeration...[/title]")
    subdomains = []
    tools = [
        ("subfinder", f"subfinder -d {domain} -o subfinder_output.txt"),
        ("amass", f"amass enum -d {domain} -o amass_output.txt"),
        ("assetfinder", f"assetfinder --subs-only {domain} > assetfinder_output.txt"),
        ("sublist3r", f"python3 Sublist3r/sublist3r.py -d {domain} -o sublist3r_output.txt")
    ]
    with Progress() as progress:
        task = progress.add_task("[cyan]Enumerating subdomains...", total=len(tools))
        for tool, command in tools:
            console.print(f"[info]Running {tool}...[/info]")
            subprocess.run(command, shell=True)
            with open(f"{tool}_output.txt", "r") as f:
                subdomains.extend(f.read().splitlines())
            progress.advance(task)
    subdomains = list(set(subdomains))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "subdomains.txt", "w") as f:
        for subdomain in subdomains:
            f.write(subdomain + '\n')
    console.print("[success]Subdomain enumeration completed! 🎉[/success]")
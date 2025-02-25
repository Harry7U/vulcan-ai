import subprocess
from pathlib import Path
from rich.console import Console
from rich.progress import Progress

OUTPUT_DIR = Path("output")

def collect_urls():
    console = Console()
    console.print("[title]🌐 Collecting URLs...[/title]")
    urls = []
    tools = [
        ("waybackurls", "cat output/subdomains.txt | waybackurls > waybackurls_output.txt"),
        ("gau", "cat output/subdomains.txt | gau > gau_output.txt"),
        ("katana", "katana -list output/subdomains.txt -o katana_output.txt")
    ]
    with Progress() as progress:
        task = progress.add_task("[cyan]Collecting URLs...", total=len(tools))
        for tool, command in tools:
            console.print(f"[info]Running {tool}...[/info]")
            subprocess.run(command, shell=True)
            with open(f"{tool}_output.txt", "r") as f:
                urls.extend(f.read().splitlines())
            progress.advance(task)
    urls = list(set(urls))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "collected_urls.txt", "w") as f:
        for url in urls:
            f.write(url + '\n')
    console.print("[success]URL collection completed! 🎉[/success]")
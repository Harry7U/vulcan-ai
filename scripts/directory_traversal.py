import openai
import requests
from pathlib import Path
from rich.console import Console

OUTPUT_DIR = Path("output")

def load_config():
    # Assuming configuration is loaded from a JSON file
    try:
        with open('configs/config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        console.print("[error]Config file not found![/error]")
        return {}
    except json.JSONDecodeError:
        console.print("[error]Error decoding the config file![/error]")
        return {}

def find_directory_traversal_vulnerabilities(urls):
    console = Console()
    config = load_config()
    openai.api_key = config.get('openai_api_key', '')

    if not openai.api_key:
        console.print("[error]OpenAI API key not found in config![/error]")
        return []

    directory_traversal_vulnerabilities = []

    for url in urls:
        prompt = f"Check if this URL is vulnerable to directory traversal: {url}"
        try:
            response = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=1024)
            result = response.choices[0].text.strip()
            if "vulnerable" in result.lower():
                directory_traversal_vulnerabilities.append(url)
        except Exception as e:
            console.print(f"[error]Error checking URL {url}: {e}[/error]")

    return directory_traversal_vulnerabilities

def run():
    console = Console()
    console.print("[title]🔍 Running directory traversal vulnerability scan...[/title]")

    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    try:
        with open(OUTPUT_DIR / "collected_urls.txt", "r") as f:
            urls = f.read().splitlines()
    except FileNotFoundError:
        console.print("[error]Collected URLs file not found![/error]")
        return

    directory_traversal_vulnerabilities = find_directory_traversal_vulnerabilities(urls)

    with open(OUTPUT_DIR / "directory_traversal_vulnerabilities.txt", "w") as f:
        for url in directory_traversal_vulnerabilities:
            f.write(url + '\n')

    console.print("[success]Directory traversal vulnerability scan completed! 🎉[/success]")

if __name__ == "__main__":
    run()

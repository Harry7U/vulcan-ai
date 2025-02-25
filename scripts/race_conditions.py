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

def find_race_conditions(urls):
    console = Console()
    config = load_config()
    openai.api_key = config.get('openai_api_key', '')

    if not openai.api_key:
        console.print("[error]OpenAI API key not found in config![/error]")
        return []

    race_condition_vulnerabilities = []

    for url in urls:
        prompt = f"Check if this URL is vulnerable to race conditions: {url}"
        try:
            response = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=1024)
            result = response.choices[0].text.strip()
            if "vulnerable" in result.lower():
                race_condition_vulnerabilities.append(url)
        except Exception as e:
            console.print(f"[error]Error checking URL {url}: {e}[/error]")

    return race_condition_vulnerabilities

def run():
    console = Console()
    console.print("[title]🔍 Running race condition vulnerability scan...[/title]")

    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    try:
        with open(OUTPUT_DIR / "collected_urls.txt", "r") as f:
            urls = f.read().splitlines()
    except FileNotFoundError:
        console.print("[error]Collected URLs file not found![/error]")
        return

    race_condition_vulnerabilities = find_race_conditions(urls)

    with open(OUTPUT_DIR / "race_condition_vulnerabilities.txt", "w") as f:
        for url in race_condition_vulnerabilities:
            f.write(url + '\n')

    console.print("[success]Race condition vulnerability scan completed! 🎉[/success]")

if __name__ == "__main__":
    run()

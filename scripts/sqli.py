import openai
import requests
from pathlib import Path
from rich.console import Console

OUTPUT_DIR = Path("output")

def load_config():
    # Assuming configuration is loaded from a JSON file
    with open('configs/config.json', 'r') as f:
        return json.load(f)

def find_sqli_vulnerabilities(urls):
    console = Console()
    config = load_config()
    openai.api_key = config['openai_api_key']
    
    sqli_vulnerabilities = []

    for url in urls:
        prompt = f"Check if this URL is vulnerable to SQL injection: {url}"
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=1024)
        result = response.choices[0].text.strip()
        if "vulnerable" in result.lower():
            sqli_vulnerabilities.append(url)
    
    return sqli_vulnerabilities

def run():
    console = Console()
    console.print("[title]🔍 Running SQL injection vulnerability scan...[/title]")

    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        
    with open(OUTPUT_DIR / "collected_urls.txt", "r") as f:
        urls = f.read().splitlines()
    
    sqli_vulnerabilities = find_sqli_vulnerabilities(urls)
    
    with open(OUTPUT_DIR / "sqli_vulnerabilities.txt", "w") as f:
        for url in sqli_vulnerabilities:
            f.write(url + '\n')
    
    console.print("[success]SQL injection vulnerability scan completed! 🎉[/success]")

if __name__ == "__main__":
    run()

import openai
import json
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

def generate_payloads(category, prompt):
    openai.api_key = load_config().get('openai_api_key', '')

    if not openai.api_key:
        console.print("[error]OpenAI API key not found in config![/error]")
        return ""

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
        console.print(f"[error]Error generating payload for {category}: {e}[/error]")
        return ""

def run():
    console = Console()
    console.print("[title]🔍 Generating AI-driven payloads for various vulnerabilities...[/title]")

    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    prompts = {
        "XSS": "Generate an XSS payload:",
        "SQLi": "Generate a SQL injection payload:",
        "SSRF": "Generate a SSRF payload:",
        "Command Injection": "Generate a command injection payload:",
        "LFI": "Generate a Local File Inclusion payload:",
        "RCE": "Generate a Remote Code Execution payload:",
        "Open Redirect": "Generate an Open Redirect payload:",
        "IDOR": "Generate an Insecure Direct Object References payload:",
        "Directory Traversal": "Generate a directory traversal payload:",
        "CSRF": "Generate a CSRF payload:",
        "CRLF Injection": "Generate a CRLF injection payload:",
        "CORS Misconfiguration": "Generate a CORS misconfiguration payload:"
    }

    payloads = {category: generate_payloads(category, prompt) for category, prompt in prompts.items()}

    with open(OUTPUT_DIR / "payloads.json", "w") as f:
        json.dump(payloads, f, indent=4)

    console.print("[success]Payload generation completed! 🎉[/success]")

if __name__ == "__main__":
    run()

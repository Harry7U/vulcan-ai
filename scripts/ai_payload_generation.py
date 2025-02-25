import openai
from pathlib import Path
from rich.console import Console

OUTPUT_DIR = Path("output")

def generate_payloads(vulnerability_type):
    console = Console()
    config = load_config()  # Assuming load_config() is defined elsewhere
    openai.api_key = config['openai_api_key']
    
    console.print(f"[title]🧠 Generating payloads for {vulnerability_type}...[/title]")
    prompt = f"Generate sophisticated payloads for {vulnerability_type} vulnerability, considering recent attack vectors."
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=1024)
    payloads = response.choices[0].text.splitlines()
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "payloads" / f"{vulnerability_type}_payloads.txt", "w") as f:
        for payload in payloads:
            f.write(payload + '\n')
    console.print(f"[success]Payload generation for {vulnerability_type} completed! 🎉[/success]")
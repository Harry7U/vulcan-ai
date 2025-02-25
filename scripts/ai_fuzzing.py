import openai
from pathlib import Path
from rich.console import Console

OUTPUT_DIR = Path("output")

def fuzz_parameters():
    console = Console()
    config = load_config()  # Assuming load_config() is defined elsewhere
    openai.api_key = config['openai_api_key']
    
    console.print("[title]🔍 AI-Driven Fuzzing...[/title]")
    prompt = "Generate intelligent wordlists for fuzzing common web application parameters."
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=1024)
    wordlists = response.choices[0].text.splitlines()
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "fuzzing_wordlist.txt", "w") as f:
        for word in wordlists:
            f.write(word + '\n')
    
    command = f"ffuf -w {OUTPUT_DIR / 'fuzzing_wordlist.txt'} -u https://example.com/FUZZ"
    console.print(f"[info]Running ffuf with AI-generated wordlist...[/info]")
    subprocess.run(command, shell=True)
    console.print("[success]AI-Driven Fuzzing completed! 🎉[/success]")

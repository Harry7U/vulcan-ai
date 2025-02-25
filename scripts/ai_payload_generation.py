import openai
import json

def load_api_key():
    with open('configs/config.json', 'r') as f:
        config = json.load(f)
    return config['openai_api_key']

def generate_payloads(category, prompt):
    openai.api_key = load_api_key()
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def run():
    prompts = {
        "XSS": "Generate an XSS payload:",
        "SQLi": "Generate a SQL injection payload:",
        "SSRF": "Generate a SSRF payload:",
        "Command Injection": "Generate a command injection payload:",
        "LFI": "Generate a Local File Inclusion payload:",
        "RCE": "Generate a Remote Code Execution payload:",
        "Open Redirect": "Generate an Open Redirect payload:",
        "IDOR": "Generate an Insecure Direct Object References payload:"
    }
    
    payloads = {category: generate_payloads(category, prompt) for category, prompt in prompts.items()}
    
    with open('output/payloads.json', 'w') as f:
        json.dump(payloads, f, indent=4)

if __name__ == "__main__":
    run()
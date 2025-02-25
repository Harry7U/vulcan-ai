import openai
import json
import subprocess

def load_api_key():
    with open('configs/config.json', 'r') as f:
        config = json.load(f)
    return config['openai_api_key']

def generate_wordlist(prompt):
    openai.api_key = load_api_key()
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip().split('\n')

def run():
    prompt = "Generate a wordlist for fuzzing:"
    wordlist = generate_wordlist(prompt)
    
    with open('output/wordlist.txt', 'w') as f:
        for word in wordlist:
            f.write(word + '\n')
    
    subprocess.run(["ffuf", "-w", "output/wordlist.txt", "-u", "http://example.com/FUZZ", "-o", "output/fuzzing_results.txt"])

if __name__ == "__main__":
    run()
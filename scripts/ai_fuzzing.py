import openai
import json
import os

def generate_wordlist(target):
    openai.api_key = "YOUR_OPENAI_API_KEY"
    
    prompt = f"Create a wordlist for directory fuzzing using common web application directories and file extensions for the target: {target}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    wordlist = response['choices'][0]['text'].strip()
    return wordlist

if __name__ == "__main__":
    target = input("Enter the target URL: ")
    
    wordlist = generate_wordlist(target)
    with open("output/wordlist.txt", "w") as f:
        f.write(wordlist)
    print(f"Wordlist saved to output/wordlist.txt")

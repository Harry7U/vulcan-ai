import openai
import json

def generate_payload(vulnerability_type, target):
    openai.api_key = "YOUR_OPENAI_API_KEY"
    
    prompt = f"Generate an advanced {vulnerability_type} payload for the target: {target}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    payload = response['choices'][0]['text'].strip()
    return payload

if __name__ == "__main__":
    target = input("Enter the target URL: ")
    vulnerability_type = input("Enter the vulnerability type (e.g., XSS, SQLi): ")
    
    payload = generate_payload(vulnerability_type, target)
    print(f"Generated payload: {payload}")

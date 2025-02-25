import subprocess
import concurrent.futures

def run_tool(tool, args):
    subprocess.run([tool] + args, shell=True)

def run(domain):
    tools = [
        ("subfinder", ["-d", domain, "-o", "output/subdomains_subfinder.txt"]),
        ("amass", ["enum", "-d", domain, "-o", "output/subdomains_amass.txt"]),
        ("assetfinder", ["--subs-only", domain, ">", "output/subdomains_assetfinder.txt"]),
        ("sublist3r", ["-d", domain, "-o", "output/subdomains_sublist3r.txt"]),
        ("findomain", ["-t", domain, "-o", "output/subdomains_findomain.txt"]),
        ("massdns", ["-r", "/path/to/resolvers.txt", domain, "-o", "output/subdomains_massdns.txt"]),
        ("dnsx", ["-d", domain, "-o", "output/subdomains_dnsx.txt"]),
        ("shuffledns", ["-d", domain, "-o", "output/subdomains_shuffledns.txt"]),
        ("puredns", ["brute", domain, "-r", "/path/to/resolvers.txt", "-w", "/path/to/wordlist.txt", "-o", "output/subdomains_puredns.txt"]),
        ("hakrevdns", ["-d", domain, "--output", "output/subdomains_hakrevdns.txt"]),
        ("chaos", ["-d", domain, "-o", "output/subdomains_chaos.txt"]),
        ("turbo", ["-d", domain, "-o", "output/subdomains_turbo.txt"])
    ]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_tool, tool, args) for tool, args in tools]
        concurrent.futures.wait(futures)
    
    # Combine results
    subdomains = set()
    for tool, args in tools:
        with open(args[-1], 'r') as f:
            subdomains.update(f.read().splitlines())
    
    with open('output/subdomains.txt', 'w') as f:
        for subdomain in sorted(subdomains):
            f.write(subdomain + '\n')

if __name__ == "__main__":
    run()
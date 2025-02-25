import subprocess
import concurrent.futures

def run_tool(tool, args):
    subprocess.run([tool] + args, shell=True)

def run(domain):
    tools = [
        ("waybackurls", ["<", "output/subdomains.txt", ">", "output/urls_waybackurls.txt"]),
        ("gau", ["-o", "output/urls_gau.txt", "--threads", "5", "-b", domain]),
        ("katana", ["-d", domain, "-o", "output/urls_katana.txt"]),
        ("getJS", ["-url", "output/subdomains.txt", "-o", "output/urls_getjs.txt"]),
        ("hakrawler", ["-url", "output/subdomains.txt", "-o", "output/urls_hakrawler.txt"]),
        ("gospider", ["-d", domain, "-o", "output/urls_gospider.txt"]),
        ("xnLinkFinder", ["-d", domain, "-o", "output/urls_xnlinkfinder.txt"]),
        ("urlgrab", ["-d", domain, "-o", "output/urls_urlgrab.txt"]),
        ("waymore", ["-d", domain, "-o", "output/urls_waymore.txt"])
    ]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_tool, tool, args) for tool, args in tools]
        concurrent.futures.wait(futures)
    
    # Combine results
    urls = set()
    for tool, args in tools:
        with open(args[-1], 'r') as f:
            urls.update(f.read().splitlines())
    
    with open('output/collected_urls.txt', 'w') as f:
        for url in sorted(urls):
            f.write(url + '\n')

if __name__ == "__main__":
    run()
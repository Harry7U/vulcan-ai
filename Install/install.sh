#!/bin/bash
# install.sh - Automated installation script for Vulcan with colorful output

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔥 Installing dependencies for Vulcan...${NC}"

# Update package lists (for Debian/Ubuntu)
if [ -x "$(command -v apt-get)" ]; then
    sudo apt-get update
fi

# Install Python dependencies
echo -e "${GREEN}🚀 Installing Python dependencies...${NC}"
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo -e "${RED}requirements.txt not found. Skipping Python dependencies installation.${NC}"
fi

# Clone and install tools
tools=(
    "https://github.com/aboul3la/Sublist3r"
    "https://github.com/projectdiscovery/subfinder"
    "https://github.com/OWASP/Amass"
    "https://github.com/tomnomnom/waybackurls"
    "https://github.com/lc/gau"
    "https://github.com/projectdiscovery/katana"
    "https://github.com/hahwul/dalfox"
    "https://github.com/sqlmapproject/sqlmap"
    "https://github.com/stasinopoulos/commix"
    "https://github.com/blechschmidt/massdns"
    "https://github.com/Findomain/Findomain"
    "https://github.com/Screetsec/Sudomy"
    "https://github.com/projectdiscovery/chaos-client"
    "https://github.com/TypeError/domained"
    "https://github.com/appsecco/bugcrowd-levelup-subdomain-enumeration"
    "https://github.com/projectdiscovery/shuffledns"
    "https://github.com/d3mondev/puredns"
    "https://github.com/christophetd/censys-subdomain-finder"
    "https://github.com/fleetcaptain/Turbolist3r"
    "https://github.com/0xbharath/censys-enumeration"
    "https://github.com/LordNeoStark/tugarecon"
    "https://github.com/cinerieus/as3nt"
    "https://github.com/si9int/Subra"
    "https://github.com/nexxai/Substr3am"
    "https://github.com/jhaddix/domain"
    "https://github.com/infosec-au/altdns"
    "https://github.com/anshumanbh/brutesubs"
    "https://github.com/lorenzog/dns-parallel-prober"
    "https://github.com/rbsec/dnscan"
    "https://github.com/guelfoweb/knock"
    "https://github.com/hakluke/hakrevdns"
    "https://github.com/projectdiscovery/dnsx"
    "https://github.com/tomnomnom/assetfinder"
    "https://github.com/nahamsec/crtndstry"
    "https://github.com/codingo/VHostScan"
    "https://github.com/edoardottt/scilla"
    "https://github.com/3nock/sub3suite"
    "https://github.com/glebarez/cero"
    "https://github.com/incogbyte/shosubgo"
    "https://github.com/hakluke/haktrails"
    "https://github.com/blacklanternsecurity/bbot"
    "https://github.com/robertdavidgraham/masscan"
    "https://github.com/RustScan/RustScan"
    "https://github.com/projectdiscovery/naabu"
    "https://github.com/nmap/nmap"
    "https://github.com/trimstray/sandmap"
    "https://github.com/johnnyxmas/ScanCannon"
    "https://github.com/FortyNorthSecurity/EyeWitness"
    "https://github.com/michenriksen/aquatone"
    "https://github.com/vladocar/screenshoteer"
    "https://github.com/sensepost/gowitness"
    "https://github.com/byt3bl33d3r/WitnessMe"
    "https://github.com/BishopFox/eyeballer"
    "https://github.com/nccgroup/scrying"
    "https://github.com/beurtschipper/Depix"
    "https://github.com/breenmachine/httpscreenshot"
    "https://github.com/AliasIO/wappalyzer"
    "https://github.com/rverton/webanalyze"
    "https://github.com/claymation/python-builtwith"
    "https://github.com/urbanadventurer/whatweb"
    "https://github.com/RetireJS/retire.js"
    "https://github.com/projectdiscovery/httpx"
    "https://github.com/praetorian-inc/fingerprintx"
    "https://github.com/OJ/gobuster"
    "https://github.com/C-Sto/recursebuster"
    "https://github.com/epi052/feroxbuster"
    "https://github.com/maurosoria/dirsearch"
    "https://github.com/evilsocket/dirsearch"
    "https://github.com/henshin/filebuster"
    "https://github.com/stefanoj3/dirstalk"
    "https://github.com/digination/dirbuster-ng"
    "https://github.com/jaeles-project/gospider"
    "https://github.com/hakluke/hakrawler"
    "https://github.com/s0rg/crawley"
    "https://github.com/GerbenJavado/LinkFinder"
    "https://github.com/zseano/JS-Scan"
    "https://github.com/arbazkiraak/LinksDumper"
    "https://github.com/0xsha/GoLinkFinder"
    "https://github.com/InitRoot/BurpJSLinkFinder"
    "https://github.com/IAmStoxe/urlgrab"
    "https://github.com/003random/getJS"
    "https://github.com/riza/linx"
    "https://github.com/xnl-h4ck3r/waymore"
    "https://github.com/xnl-h4ck3r/xnLinkFinder"
    "https://github.com/commixproject/commix"
    "https://github.com/s0md3v/Corsy"
    "https://github.com/RUB-NDS/CORStest"
    "https://github.com/laconicwolf/cors-scanner"
    "https://github.com/Shivangx01b/CorsMe"
    "https://github.com/Nefcore/CRLFsuite"
    "https://github.com/dwisiswant0/crlfuzz"
    "https://github.com/MichaelStott/CRLF-Injection-Scanner"
    "https://github.com/BountyStrike/Injectus"
    "https://github.com/0xInfection/XSRFProbe"
    "https://github.com/wireghoul/dotdotpwn"
    "https://github.com/chrispetrou/FDsploit"
    "https://github.com/bayotop/off-by-slash"
    "https://github.com/momenbasel/liffier"
    "https://github.com/mzfr/liffy"
    "https://github.com/Team-Firebugs/Burp-LFI-tests"
    "https://github.com/mthbernardes/LFI-Enum"
    "https://github.com/D35m0nd142/LFISuite"
    "https://github.com/hussein98d/LFI-files"
    "https://github.com/doyensec/inql"
    "https://github.com/swisskyrepo/GraphQLmap"
    "https://github.com/szski/shapeshifter"
    "https://github.com/zidekmat/graphql_beautifier"
    "https://github.com/nikitastupin/clairvoyance"
    "https://github.com/vanhauser-thc/thc-hydra"
    "https://github.com/ihebski/DefaultCreds-cheat-sheet"
    "https://github.com/ztgrace/changeme"
    "https://github.com/1N3/BruteX"
    "https://github.com/lanjelot/patator"
    "https://github.com/awslabs/git-secrets"
    "https://github.com/zricethezav/gitleaks"
    "https://github.com/dxa4481/truffleHog"
    "https://github.com/hisxo/gitGraber"
    "https://github.com/thoughtworks/talisman"
    "https://github.com/BishopFox/GitGot"
    "https://github.com/anshumanbh/git-all-secrets"
    "https://github.com/gwen001/github-search"
    "https://github.com/cve-search/git-vuln-finder"
    "https://github.com/x1sec/commit-stream"
    "https://github.com/michenriksen/gitrob"
    "https://github.com/auth0/repo-supervisor"
    "https://github.com/UnkL4b/GitMiner"
    "https://github.com/eth0izzle/shhgit"
    "https://github.com/Yelp/detect-secrets"
    "https://github.com/newrelic/rusty-hog"
    "https://github.com/Skyscanner/whispers"
    "https://github.com/nielsing/yar"
    "https://github.com/BishopFox/dufflebag"
    "https://github.com/duo-labs/secret-bridge"
    "https://github.com/americanexpress/earlybird"
    "https://github.com/trufflesecurity/Trufflehog-Chrome-Extension"
    "https://github.com/praetorian-inc/noseyparker"
    "https://github.com/internetwache/GitTools"
    "https://github.com/liamg/gitjacker"
    "https://github.com/arthaud/git-dumper"
    "https://github.com/digininja/GitHunter"
    "https://github.com/kost/dvcs-ripper"
    "https://github.com/praetorian-inc/gato"
)

for tool in "${tools[@]}"; do
    git clone $tool
done

# Make install.sh executable
chmod +x install.sh

# Generate payloads for all vulnerability types
echo -e "${GREEN}🔧 Generating payloads for all vulnerability types...${NC}"
python3 ai_payload_generation.py

# Integrate with other scripts for vulnerability testing
echo -e "${GREEN}🔗 Integrating with other scripts for vulnerability testing...${NC}"
python3 ai_fuzzing.py
python3 vulnerability_testing.py

echo -e "${GREEN}✅ Installation complete. Configure your API keys and sensitive data in 'config/config.json'.${NC}"

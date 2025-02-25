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
    "https://github.com/aboul3la/Sublist3r.git"
    "https://github.com/projectdiscovery/subfinder.git"
    "https://github.com/OWASP/Amass.git"
    "https://github.com/tomnomnom/waybackurls.git"
    "https://github.com/lc/gau.git"
    "https://github.com/projectdiscovery/katana.git"
    "https://github.com/hahwul/dalfox.git"
    "https://github.com/sqlmapproject/sqlmap.git"
    "https://github.com/stasinopoulos/commix.git"
)

for tool in "${tools[@]}"; do
    git clone $tool
done

# Make install.sh executable
chmod +x install.sh

echo -e "${GREEN}✅ Installation complete. Configure your API keys and sensitive data in 'config/config.json'.${NC}"

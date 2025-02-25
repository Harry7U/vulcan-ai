# 🌋 Vulcan AI 🌋

Welcome to **Vulcan AI**! This repository contains various tools and scripts to automate the process of vulnerability assessment and exploitation. Below you'll find detailed steps on how to install, configure, and use Vulcan AI effectively.

## 🚀 Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Tools Included](#tools-included)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Introduction

Vulcan AI is designed to help security researchers and penetration testers automate the process of finding and exploiting vulnerabilities. With a wide range of tools included, Vulcan AI covers various aspects of reconnaissance, scanning, and exploitation.

## 🛠️ Installation

Follow these steps to install Vulcan AI:

### Prerequisites

- Python 3.x
- Git

### Steps

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Harry7U/vulcan-ai.git
    cd vulcan-ai
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Installation Script**
    ```bash
    chmod +x Install/install.sh
    ./Install/install.sh
    ```

    This script will:
    - Install necessary Python dependencies.
    - Clone and install various tools required for vulnerability assessment.

## 🛠 Configuration

Update the `config.json` file with your API keys and other sensitive data.

### Example Configuration
```json
{
  "openai_api_key": "YOUR_OPENAI_API_KEY",
  "other_sensitive_data": {
    "example": "value"
  },
  "settings": {
    "max_threads": 10,
    "timeout": 60,
    "color_theme": "vibrant",
    "enable_animations": true
  }
}
```

## 🎮 Usage

Once everything is set up, you can start using Vulcan AI for various tasks.

### Generate Payloads
```bash
python3 scripts/ai_payload_generation.py
```

### Fuzzing
```bash
python3 scripts/ai_fuzzing.py
```

### Vulnerability Testing
```bash
python3 scripts/vulnerability_testing.py
```

## 🔧 Tools Included

### Reconnaissance
- **Subdomain Enumeration**: subfinder, amass, assetfinder, sublist3r, findomain
- **URL Collection**: waybackurls, gau, katana
- **Port Scanning**: nmap, rustscan
- **Screenshotting**: eyewitness, gowitness
- **Technology Identification**: wappalyzer, httpx
- **Content Discovery**: gobuster, feroxbuster

### Exploitation
- **Command Injection**: commix
- **CORS Misconfiguration**: Corsy
- **CRLF Injection**: CRLFsuite
- **CSRF Injection**: XSRFProbe
- **Directory Traversal**: dotdotpwn
- **File Inclusion**: liffy
- **GraphQL Injection**: GraphQLmap
- **Miscellaneous**: thc-hydra, changeme, git-secrets, gitleaks, GitTools, S3Scanner
- **Fuzzing**: ffuf

## 🤝 Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

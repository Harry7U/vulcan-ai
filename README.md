# Vulcan - Hunter's Arsenal 🔍

## Overview

**Vulcan** is an advanced, AI-driven bug bounty hunting tool designed to automate the complete security assessment process. Drawing inspiration from the Roman god of fire, metalworking, and craftsmanship, our tool embodies the power of creation and destruction in cybersecurity.

Enjoy a modern CLI experience enhanced with vibrant colors, dynamic animations, and engaging emojis for real-time feedback during scans.

## Key Features

- **Modular Architecture:** Well-organized directory structure for easy maintenance.
- **Dynamic & Colorful CLI:** Leveraging [rich](https://github.com/willmcgugan/rich) and [colorama](https://github.com/tartley/colorama) for improved output.
- **AI-Driven Payload Generation:** Utilizing the OpenAI API for smart payloads.
- **Parallel Processing:** Multi-threading for accelerated scanning.
- **Secure Configuration:** Sensitive data stored safely in `config/config.json`.
- **Comprehensive Reporting:** Generate reports in JSON, CSV, and custom formats.
- **Plugin Support:** Easily extendable with dedicated plugins.

## Directory Structure

```
Vulcan/
├── config/
│   └── config.json
├── output/
│   ├── subdomains.txt
│   ├── collected_urls.txt
│   ├── categorized_urls/
│   │   ├── xss.txt
│   │   ├── sqli.txt
│   │   └── ssrf.txt
│   ├── payloads/
│   │   ├── xss_payloads.txt
│   │   ├── sqli_payloads.txt
│   │   └── ssrf_payloads.txt
│   ├── testing_results/
│   │   ├── xss_results.txt
│   │   ├── sqli_results.txt
│   │   └── ssrf_results.txt
│   └── reports/
│       ├── json_report.json
│       ├── csv_report.csv
│       └── custom_report.txt
├── plugins/
│   ├── xss_plugin.py
│   ├── sqli_plugin.py
│   ├── ssrf_plugin.py
│   └── ...
├── tools/
│   ├── subfinder
│   ├── amass
│   ├── assetfinder
│   ├── waybackurls
│   ├── gau
│   ├── katana
│   ├── dalfox
│   ├── sqlmap
│   ├── commix
│   ├── sublist3r
│   └── ...
├── ai_fuzzing.py
├── ai_payload_generation.py
├── main.py
├── report_generation.py
├── subdomain_enumeration.py
├── url_collection.py
├── vulnerability_filtering.py
├── vulnerability_testing.py
├── install.sh
└── README.md
```

## Installation

Run the installation script to set up dependencies and external tools:

```bash
bash install.sh
```

## Usage

The CLI options include:

- `--recon` or `-r`: Run reconnaissance modules.
- `--fuzz` or `-f`: Run fuzzing modules.
- `--exploit` or `-e`: Run exploitation modules.
- `--generate` or `-g`: Generate AI-based payloads.
- `--report` or `-rp`: Generate comprehensive reports.
- `--feedback` or `-fb`: Submit user feedback.
- `--all` or `-a`: Execute the full workflow.

Example:

```bash
python main.py --all
```

## Contributing

Contributions are welcome! Please fork the repo and open a pull request with your improvements.

## License

MIT License
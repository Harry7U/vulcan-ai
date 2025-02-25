import argparse
import logging
import os
from scripts import ai_payload_generation, ai_fuzzing, vulnerability_testing

def setup_logging():
    if not os.path.exists("output/logs"):
        os.makedirs("output/logs")
    logging.basicConfig(
        filename='output/logs/vulcan_ai.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Vulcan AI: AI-Powered Penetration Testing Framework")
    subparsers = parser.add_subparsers(dest="command")

    parser_payload = subparsers.add_parser("generate_payload", help="Generate AI-enhanced payloads")
    parser_payload.add_argument("vulnerability_type", type=str, help="Type of vulnerability (e.g., XSS, SQLi)")
    parser_payload.add_argument("target", type=str, help="Target URL")

    parser_fuzz = subparsers.add_parser("fuzz", help="Perform AI-enhanced fuzzing")
    parser_fuzz.add_argument("target", type=str, help="Target URL")

    parser_test = subparsers.add_parser("test", help="Perform vulnerability testing")
    parser_test.add_argument("target", type=str, help="Target URL")

    args = parser.parse_args()

    if args.command == "generate_payload":
        ai_payload_generation.generate_payload(args.vulnerability_type, args.target)
    elif args.command == "fuzz":
        ai_fuzzing.fuzz(args.target)
    elif args.command == "test":
        vulnerability_testing.test(args.target)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

import json
import csv

def generate_json_report(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def generate_csv_report(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data.keys())
        writer.writerows(zip(*data.values()))

def run():
    with open('output/testing_results/dalfox_xss.txt', 'r') as f:
        xss_results = f.read().splitlines()
    
    with open('output/testing_results/sqlmap_sqli.txt', 'r') as f:
        sqli_results = f.read().splitlines()
    
    with open('output/testing_results/commix_cmd.txt', 'r') as f:
        cmd_results = f.read().splitlines()
    
    report_data = {
        "XSS": xss_results,
        "SQLi": sqli_results,
        "Command Injection": cmd_results
    }
    
    generate_json_report(report_data, 'output/reports/report.json')
    generate_csv_report(report_data, 'output/reports/report.csv')

if __name__ == "__main__":
    run()
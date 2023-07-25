import requests
import json
import sys
import subprocess
from tqdm import tqdm


def print_banner():
    banner = """
  ____        _       ____        _            
 / ___| _   _| |__   / ___| _ __ (_)_ __   ___ 
 \___ \| | | | '_ \  \___ \| '_ \| | '_ \ / _ \\
  ___) | |_| | |_) |  ___) | | | | | |_) |  __/
 |____/ \__,_|_.__/  |____/|_| |_|_| .__/ \___|
                   By:Thee Eclipse |_|
                   Twitter:@Thee_Eclipse
    """
    print(banner)

def fetch_subdomains(domain):
    url = f'https://crt.sh/?q=%.{domain}&output=json'
    response = requests.get(url)
    json_data = json.loads(response.text)
    subdomains = [item['name_value'] for item in json_data]
    subdomains = list(set(subdomains))
    return subdomains

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        domains = f.read().splitlines()

    with open(output_file, 'w') as f_out:
        for domain in tqdm(domains, desc="Fetching Subdomains", unit="domain"):
            subdomains = fetch_subdomains(domain)
            for subdomain in subdomains:
                f_out.write(subdomain + '\n')

 # Subfinder runs from here
    subprocess.run(['/home/ubuntu/go/bin/subfinder', '-dL', input_file, '-o', output_file])

if __name__ == "__main__":
    print_banner()  
    if len(sys.argv) != 5 or sys.argv[1] != '-f' or sys.argv[3] != '-o':
        print("Usage: python3 script.py -f input_domains.txt -o output_subdomains.txt")
        sys.exit(1)

    input_file = sys.argv[2]
    output_file = sys.argv[4]
    main(input_file, output_file)

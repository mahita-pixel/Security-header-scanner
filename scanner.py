import requests
from colorama import Fore, init

init(autoreset=True)

SECURITY_HEADERS = {
    "Strict-Transport-Security": "HSTS",
    "Content-Security-Policy": "CSP",
    "X-Frame-Options": "Clickjacking Protection",
    "X-Content-Type-Options": "MIME Type Protection",
    "Referrer-Policy": "Referrer Protection",
    "Permissions-Policy": "Permissions Policy"
}

def check_headers(url):
    try:
        response = requests.get(url, timeout=10)

        print(f"\nScanning: {url}")
        print("-" * 50)

        score = 0

        for header, description in SECURITY_HEADERS.items():
            if header in response.headers:
                print(Fore.GREEN + f"[+] {header} Found")                
                score += 1
            else:
                print(Fore.RED + f"[-] {header} Missing")

        print("-" * 50)
        print(f"Security Score: {score}/{len(SECURITY_HEADERS)}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = input("Enter website URL (https://example.com): ")
    check_headers(target)
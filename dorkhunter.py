#!/usr/bin/env python3
"""
DorkHunter © 2025 by Ali Mrad – Bug Bounty Hunter.
All rights reserved.
Unauthorized reproduction or distribution of this tool or any portion of it may result in severe civil and criminal penalties.

"""

import requests
import time

# Your SerpAPI Key
API_KEY = "UR API HERE"

# Dork definitions
dorks = {
    "1. Directory listing vulnerabilities": 'site:{site} intitle:"index of"',
    "2. Exposed Configuration files": 'site:{site} (ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini)',
    "3. Exposed Database files": 'site:{site} (ext:sql | ext:dbf | ext:mdb)',
    "4. Find WordPress": 'site:{site} (inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download)',
    "5. Exposed log files": 'site:{site} ext:log',
    "6. Backup and old files": 'site:{site} (ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup)',
    "7. Login pages": 'site:{site} inurl:login',
    "8. SQL errors": (
        'site:{site} (intext:"sql syntax near" | intext:"syntax error has occurred" | '
        'intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | '
        'intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()")'
    ),
    "9. Publicly exposed documents": 'site:{site} (ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv)',
    "10. Employees on LINKEDIN": 'site:linkedin.com employees {site}',
    "11. Find Subdomains": 'site:*.{site}',
    "12. Find Sub-Subdomains": 'site:*.*.{site}'
}

def search_all_pages(query, max_pages=100):
    all_links = []
    start = 0
    results_per_page = 10
    for page in range(max_pages):
        print(f"[+] Fetching page {page + 1}...")
        params = {
            "engine": "google",
            "q": query,
            "api_key": API_KEY,
            "start": start
        }
        url = "https://serpapi.com/search.json"
        response = requests.get(url, params=params)
        data = response.json()

        results = data.get("organic_results", [])
        if not results:
            print("[!] No more results found.")
            break

        for result in results:
            link = result.get("link")
            if link:
                all_links.append(link)

        start += results_per_page
        time.sleep(1.5)  # polite delay to avoid being blocked or throttled

    return all_links

def main():
    print("==== 🛡️  DorkHunter | by Ali Mrad ====\n")
    site = input("🌐 Enter target website (e.g., example.com): ").strip()

    print("\n🔍 Choose a dork to use:")
    for key in dorks:
        print("   " + key)

    choice = input("\n👉 Enter the number of the dork to use (e.g., 1): ").strip()
    selected_key = next((k for k in dorks if k.startswith(choice + ".")), None)
    if not selected_key:
        print("[-] Invalid choice.")
        return

    dork_template = dorks[selected_key]
    dork_query = dork_template.format(site=site)

    print(f"\n[+] Running Dork: {dork_query}")
    links = search_all_pages(dork_query)

    output_file = f"dorkhunter_results_{choice}.txt"
    with open(output_file, "w") as f:
        for link in links:
            f.write(link + "\n")

    print(f"\n✅ Total Links Found: {len(links)}")
    print(f"📁 Saved to: {output_file}\n")

if __name__ == "__main__":
    main()

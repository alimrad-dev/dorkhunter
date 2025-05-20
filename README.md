# dorkhunter
DorkHunter is a powerful Google Dork automation tool designed for security researchers and bug bounty hunters. It allows users to discover publicly exposed sensitive files, directories, configurations, backups, login pages, and much more across any target website using curated Google Dorks.  
**Created by Ali Mrad, Bug Bounty Hunter**

**✨ Features**

Easy-to-use terminal interface Multiple Google Dork presets (WordPress, SQL Errors, Public Documents, Config Files, etc.)
User-input for target site
Automatically scrapes all result pages
Saves found links to results.txt



**📁 Installation**

Clone the repository:
`git clone https://github.com/yourusername/BugDorker.git`

`cd BugDorker`

Install dependencies:
`pip install -r requirements.txt`

Get a SerpAPI Key:
Go to: **`https://serpapi.com/users/sign_up`**
Sign up and verify your email
Copy your API key from your dashboard

Configure your API key to the code:

**Line 13 in the code: API_KEY = "UR API KEY HERE"**



**💻 Usage**

**`python bugdorker.py`**

Enter the domain or site (e.g., target.com)

Choose one of the dork categories (Number)

The tool will collect and save all found links to results.txt



**📊 Dork Categories**

**1) Directory Listing Vulnerabilities**

**2) Exposed Configuration Files**

**3) Exposed Database Files**

**4) WordPress Installation Info**

**5) Exposed Log Files**

**6) Backup & Old Files**

**7) Login Pages**

**8) SQL Error Messages**

**9) Publicly Exposed Documents**

**10) Employees on LinkedIn**

**11) Subdomain Finder**

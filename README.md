# dorkhunter
DorkHunter is a powerful Google Dork automation tool designed for security researchers and bug bounty hunters. It allows users to discover publicly exposed sensitive files, directories, configurations, backups, login pages, and much more across any target website using curated Google Dorks.  Created by Ali Mrad, Bug Bounty Hunter
✨ Features

Easy-to-use terminal interface

Multiple Google Dork presets (WordPress, SQL Errors, Public Documents, Config Files, etc.)

User-input for target site

Automatically scrapes all result pages

Saves found links to results.txt

📁 Installation

Clone the repository:

git clone https://github.com/yourusername/BugDorker.git
cd BugDorker

Install dependencies:

pip install -r requirements.txt

Get a SerpAPI Key:

Go to: https://serpapi.com/users/sign_up

Sign up and verify your email

Copy your API key from your dashboard

Configure your API key:

Create a .env file in the project folder:

echo "SERPAPI_KEY=your_api_key_here" > .env

💻 Usage

python bugdorker.py

Enter the domain or site (e.g., recreation.gov or target.com)

Choose one of the dork categories

The tool will collect and save all found links to results.txt

📊 Dork Categories

Directory Listing Vulnerabilities

Exposed Configuration Files

Exposed Database Files

WordPress Installation Info

Exposed Log Files

Backup & Old Files

Login Pages

SQL Error Messages

Publicly Exposed Documents

Employees on LinkedIn

Subdomain Finder

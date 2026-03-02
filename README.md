# URL_Phishing_Detector(Rule Based)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Status](https://img.shields.io/badge/Status-Active-green)

# 🛡️ Heuristic-Based Phishing URL Detector

A modular, rule-based phishing URL detection system built in Python.

This project detects potentially malicious URLs using heuristic analysis techniques commonly used in lightweight security scanners.

---

## 🚀 Project Overview

Phishing websites often use tricks such as:

- Excessive subdomains
- Suspicious keywords
- Raw IP addresses instead of domain names
- URL shorteners
- Suspicious top-level domains
- Special character obfuscation

This tool analyzes a given URL and flags suspicious indicators based on multiple independent security rules.

---

## 🏗️ Project Architecture

Phishing-Detector/
│
├── main.py              # CLI interface
├── url_analyzer.py      # Rule engine & classification logic
├── rules.py             # Individual phishing detection rules
└── README.md

### 🔹 rules.py
Contains individual heuristic checks.
Each rule:
- Checks exactly one condition
- Returns True or False
- Does not calculate risk score

### 🔹 url_analyzer.py
- Runs all rules
- Collects triggered indicators
- Calculates risk level

### 🔹 main.py
- Accepts user input
- Displays structured security report

---

## 🔎 Detection Rules Implemented

- Excessive URL length (>100 characters)
- Too many subdomains
- Presence of '@' symbol
- IP address used instead of domain
- Suspicious phishing keywords
- Missing HTTPS
- Multiple hyphens in domain
- URL shortener usage
- Suspicious TLD (.tk, .ml, .ga, etc.)
- Double slash redirect trick (//)

---

## ⚙️ Installation & Usage

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/phishing-detector.git
cd phishing-detector
```
### 2️⃣ Run the Tool
```
python main.py
```
### 3️⃣ Enter URL
```
http://192.168.1.1/login-secure-update.tk
```

🧠 Risk Classification Logic
| Triggered Indicators | Risk Level  |
| -------------------- | ----------- |
| 0                    | SAFE        |
| 1                    | LOW RISK    |
| 2–3                  | MEDIUM RISK |
| 4+                   | HIGH RISK   |

📌 Example Output : 
==================================================
        PHISHING URL DETECTOR
     Heuristic-Based Scanner
==================================================

Enter URL to analyze:
http://192.168.1.1/login-secure-update.tk

--------------------------------------------------
URL: http://192.168.1.1/login-secure-update.tk
Risk Level: HIGH RISK
Triggered Indicators: 5
--------------------------------------------------

⚠ Indicators Found:
 - Uses IP address instead of domain
 - Contains phishing keywords
 - Does not use HTTPS
 - Suspicious top-level domain
 - Multiple hyphens in domain

Scan Completed.

## Author
Satwik Mishra  
B.Tech CSE (Cybersecurity)  
Security Learner | Frontend Developer

# URL_Phishing_Detector(Rule Based)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Project Overview

The URL Phishing Detection Tool is a rule-based cybersecurity project that analyzes URLs 
and determines whether they are Safe, Suspicious, or Likely Phishing.

This tool detects common phishing patterns using predefined security rules 
such as suspicious keywords, IP-based URLs, excessive length, HTTP usage, 
and domain anomalies.

This project was built to strengthen practical knowledge in defensive security 
and understand real-world phishing attack techniques.

## Features

- Detects use of IP address in URL
- Checks URL length
- Identifies suspicious keywords
- Detects HTTP instead of HTTPS
- Checks excessive subdomains
- Detects hyphen in domain name
- Risk scoring system
- CLI-based user interaction
- Scan history logging

## How It Works

The tool follows these steps:

1. User inputs a URL.
2. The URL is parsed and analyzed.
3. Multiple phishing detection rules are applied.
4. Each rule contributes to a risk score.
5. Based on the final score, the URL is classified as:

   - Safe
   - Suspicious
   - Likely Phishing

## Risk Scoring System

Each suspicious indicator adds 1 point to the risk score.

| Risk Score |          Verdict     |
|------------|----------------------|
| 0 - 2      |      Safe            | 
| 3 - 4      |      Suspicious      |
| 5+         |      Likely Phishing |

## Usage

Run the main file:

    python main.py

Enter a URL when prompted.

Example:

    Enter a URL: http://paypal-secure-login.com

Output:

    Risk Score: 4
    Verdict: Suspicious

## Learning Outcomes

- Understanding phishing attack patterns
- Writing modular Python code
- Implementing rule-based detection systems
- Risk scoring methodology
- Defensive security mindset

## Author

Satwik Mishra  
B.Tech CSE (Cybersecurity)  
Security Learner | Python Developer

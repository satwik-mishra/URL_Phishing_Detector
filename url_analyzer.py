# This is the brain of this tool
""" Its Responsibilities are :

To call rule functions from rules.py
To collect triggered rules
To calculate score
To decide final verdict """
import rules


def analyze_url(url):
    triggered_rules = []

    if rules.long_url(url):
        triggered_rules.append("URL is too long")

    if rules.too_many_dots(url):
        triggered_rules.append("Too many dots (possible subdomain abuse)")

    if rules.has_at_symbol(url):
        triggered_rules.append("Contains @ symbol")

    if rules.has_ip_address(url):
        triggered_rules.append("Uses IP address instead of domain")

    if rules.has_suspicious_keywords(url):
        triggered_rules.append("Contains suspicious keywords")

    if rules.no_https(url):
        triggered_rules.append("Does not use HTTPS")

    if rules.has_hyphen(url):
        triggered_rules.append("Contains hyphen in domain")

    if rules.is_shortened_url(url):
        triggered_rules.append("Uses URL shortening service")

    if rules.suspicious_tld(url):
        triggered_rules.append("Uses suspicious top-level domain")

    score = len(triggered_rules)

    # Decision logic
    if score >= 3:
        verdict = "⚠️ HIGH RISK - Likely Phishing"
    elif score == 2:
        verdict = "⚠️ MEDIUM RISK - Suspicious"
    elif score == 1:
        verdict = "⚠️ LOW RISK - Slightly Suspicious"
    else:
        verdict = "✅ SAFE - No strong phishing indicators"

    return verdict, triggered_rules
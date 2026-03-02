"""
Each rule:
- Checks only ONE condition
- Returns True or False
- Does NOT calculate score
"""

import re
from urllib.parse import urlparse


def extract_domain(url):
    """
    Extract domain safely from URL.
    """
    parsed = urlparse(url)
    return parsed.netloc


# ---------------------------
# Length Based Rule
# ---------------------------

def long_url(url):
    """
    Very long URLs are commonly used in phishing.
    """
    return len(url) > 100


# ---------------------------
# Subdomain Abuse
# ---------------------------

def too_many_dots(url):
    """
    Excessive subdomains are suspicious.
    """
    domain = extract_domain(url)
    return domain.count('.') > 2


# ---------------------------
# @ Symbol Trick
# ---------------------------

def has_at_symbol(url):
    """
    Attackers use @ to hide real destination.
    """
    return "@" in url


# ---------------------------
# IP Address Instead of Domain
# ---------------------------

def has_ip_address(url):
    """
    Detect raw IPv4 address usage.
    """
    domain = extract_domain(url)
    ip_pattern = r"^\d+\.\d+\.\d+\.\d+$"
    return re.match(ip_pattern, domain) is not None


# ---------------------------
# Suspicious Keywords
# ---------------------------

def has_suspicious_keywords(url):
    """
    Common phishing lure words.
    """
    keywords = [
        "login", "verify", "secure",
        "account", "bank", "update",
        "confirm", "password", "signin"
    ]

    url_lower = url.lower()
    return any(word in url_lower for word in keywords)


# ---------------------------
# HTTPS Check
# ---------------------------

def no_https(url):
    """
    Phishing sites often avoid HTTPS.
    """
    return not url.lower().startswith("https://")


# ---------------------------
# Hyphen Abuse
# ---------------------------

def has_hyphen(url):
    """
    Multiple hyphens in domain look suspicious.
    """
    domain = extract_domain(url)
    return domain.count('-') >= 2


# ---------------------------
# URL Shortener Detection
# ---------------------------

def is_shortened_url(url):
    """
    Shorteners hide actual destination.
    """
    domain = extract_domain(url)

    shorteners = [
        "bit.ly", "tinyurl.com", "goo.gl",
        "t.co", "is.gd", "buff.ly"
    ]

    return domain in shorteners


# ---------------------------
# Suspicious TLD
# ---------------------------

def suspicious_tld(url):
    """
    Cheap/free TLDs commonly abused.
    """
    domain = extract_domain(url)

    suspicious_tlds = [
        ".tk", ".ml", ".ga",
        ".cf", ".gq", ".xyz", ".top"
    ]

    return any(domain.endswith(tld) for tld in suspicious_tlds)


# ---------------------------
# Double Slash Redirect Trick
# ---------------------------

def has_double_slash_redirect(url):
    """
    Example:
    http://example.com//malicious.com
    """
    return url.count("//") > 1
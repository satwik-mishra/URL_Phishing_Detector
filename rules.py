""" Each rule should:

Check one condition

Return True or False

Not calculate score """
import re
def long_url(url):
    return len(url)>75  # this will return true if the length of url is more than 75 characters

def too_many_dots(url):
    return url.count('.')>3  #phising URLs have too many subdomains thats why we are checking whether the number of subdomains are more than 3

def has_at_symbol(url):
    return "@" in url

def has_ip_address(url):
    ip_pattern = r"http[s]?://\d+\.\d+\.\d+\.\d+"
    return re.search(ip_pattern, url) is not None

def has_suspicious_keywords(url): 
    keywords = ["login", "verify", "secure", "account", "bank", "update"]   # these are common phishing words
    for word in keywords:
        if word in url.lower():
            return True
    return False

def no_https(url):
    return not url.startswith("https://")

def has_hyphen(url):
    return "-" in url

def is_shortened_url(url):
    shorteners = ["bit.ly", "tinyurl.com", "goo.gl", "t.co"]
    for shortener in shorteners:
        if shortener in url:
            return True
    return False

def suspicious_tld(url):
    suspicious_domains = [".tk", ".ml", ".ga", ".cf", ".gq"]
    for tld in suspicious_domains:
        if url.endswith(tld):
            return True
    return False
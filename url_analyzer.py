import rules


def analyze_url(url):
    triggered = []

    # Map rule functions to readable names
    rule_checks = {
        "URL is excessively long": rules.long_url,
        "Too many subdomains detected": rules.too_many_dots,
        "Contains @ symbol": rules.has_at_symbol,
        "Uses IP address instead of domain": rules.has_ip_address,
        "Contains phishing keywords": rules.has_suspicious_keywords,
        "Does not use HTTPS": rules.no_https,
        "Multiple hyphens in domain": rules.has_hyphen,
        "Uses URL shortener": rules.is_shortened_url,
        "Suspicious top-level domain": rules.suspicious_tld,
        "Possible redirect using // trick": rules.has_double_slash_redirect,
    }

    # Run all rules
    for description, rule_function in rule_checks.items():
        try:
            if rule_function(url):
                triggered.append(description)
        except Exception:
            # Safety in case malformed URL causes crash
            continue

    score = len(triggered)

    # Risk Classification
    if score >= 4:
        risk = "HIGH RISK"
    elif score >= 2:
        risk = "MEDIUM RISK"
    elif score == 1:
        risk = "LOW RISK"
    else:
        risk = "SAFE"

    return {
        "url": url,
        "score": score,
        "risk": risk,
        "triggered_rules": triggered
    }
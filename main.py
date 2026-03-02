from url_analyzer import analyze_url


def print_banner():
    print("=" * 50)
    print("        PHISHING URL DETECTOR")
    print("     Heuristic-Based Scanner")
    print("=" * 50)


def main():
    print_banner()

    url = input("\nEnter URL to analyze: ").strip()

    result = analyze_url(url)

    print("\n" + "-" * 50)
    print(f"URL: {result['url']}")
    print(f"Risk Level: {result['risk']}")
    print(f"Triggered Indicators: {result['score']}")
    print("-" * 50)

    if result["triggered_rules"]:
        print("\n⚠ Indicators Found:")
        for rule in result["triggered_rules"]:
            print(f" - {rule}")
    else:
        print("\n✅ No suspicious indicators detected.")

    print("\nScan Completed.\n")


if __name__ == "__main__":
    main()
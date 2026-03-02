""" Responsibility:
It will take URL input
Then it will Call url_analyzer
and then Print the result clearly """
from url_analyzer import analyze_url


def main():
    print("===================================")
    print("      PHISHING URL DETECTOR        ")
    print("===================================\n")

    url = input("Enter URL to analyze: ").strip()

    verdict, triggered_rules = analyze_url(url)

    print("\n-----------------------------------")
    print("RESULT:")
    print("-----------------------------------")
    print(verdict)

    if triggered_rules:
        print("\nTriggered Rules:")
        for rule in triggered_rules:
            print(f"- {rule}")
    else:
        print("\nNo suspicious indicators detected.")

    print("\nAnalysis Complete.")


if __name__ == "__main__":
    main()
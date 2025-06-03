import requests
from get_tos import get_text_url
from summarize import claude_summary
from risk_level import risk_level

def analyze_website(url):
    tos_text = get_text_url(url)
    if "Error" in tos_text:
        return tos_text
    print("Loading Summary ...")
    summary = claude_summary(tos_text)

    print("Analyzing risk level ...")
    rating = risk_level(tos_text)

    return{
        "summary":summary,
        "rating": rating
    }

if __name__ == "__main__":
    output = analyze_website("https://www.linkedin.com/legal/user-agreement")

    print("\n---Summary---")
    print(output["summary"])
    print("\n---Risk Level---")
    print(output["rating"])

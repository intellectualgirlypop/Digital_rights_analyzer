import requests
from get_tos import get_text_url,get_tos_url
from summarize import claude_summary
from risk_level import risk_level

def analyze_website(url):
    tos_url = get_tos_url(url)
    if not tos_url:
        return "Terms of service page not found. :( "
    print("Found ToS:" + str(tos_url))

    tos_text = get_text_url(tos_url)
    if "Error" in tos_text:
        return tos_text
    print("Loading Summary ...")
    summary = claude_summary(tos_text)

    print("Analyzing risk level ...")
    rating = risk_level(tos_text)

    return{
        "tos_url":tos_url,
        "summary":summary,
        "rating": rating
    }

if __name__ == "__main__":
    output = analyze_website("https://www.linkedin.com")

    print("\n---Summary---")
    print(output+"summary")
    print("\n---Risk Level---")
    print(output+"rating")
#L1
import os
#L2
import anthropic
#F
client = anthropic.Anthropic(api_key=os.getenv("your-api-key"))

def claude_summary(text,model="claude-3-5-haiku-20241022"):
    try:
        message = client.messages.create(
            model=model,
            max_tokens=800,
            temperature=0.5,
            system="You are a digital rights clarity assistant. Summarize and simplify Terms of Service documents in user-friendly language.",
            messages=[
                {"role":"user","content": f"Summarize the following Terms of Service in clear and easy to understand language. Highlight user right, obligations, data usage, and any risky clauses:\n\n{text}"}
            ]
        )

        return message.content[0].text.strip()
    except Exception as e:
        return "Error summarizing text with Claude:" +str(e)

if __name__ == "__main__":
    tos_text = """
    By using our services, you agree to our data collection practices. We may share anonymized data with third parties.
    You are responsible for your account security. Violation of these terms may result in account termination.
    """
    summary = claude_summary(tos_text)
    print("📄 Summary:\n")
    print(summary)
import re

def risk_level(text):

    red_flags = ["no liability","without notice", "you agree to", "we reserve the right",
                  "data sharing"," non-refundable","arbitration"]
    yellow_flags =["usage data", "some information","may","can","possibly"]

    red_count = 0
    for words in red_flags:
        if re.search(words,text,re.IGNORECASE):
            red_count += 1    
    
    yellow_count = 0
    for words in yellow_flags:
        if re.search(words,text,re.IGNORECASE):
            yellow_count += 1    
    
    if red_count >= 3:
        risk ="🔴 RED -High Risk Terms"
    elif yellow_count >= 3:
        risk ="🟡YELLOW- Proceed with Caution"
    else:
        risk = "🟢GREEN- Fair Terms "
        
    return risk


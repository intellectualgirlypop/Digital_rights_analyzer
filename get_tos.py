#L1
import requests
#L2
import os
#L3
import anthropic

#C1
client = anthropic.Anthropic(api_key=os.getenv("your-api-key"))

#F1
def get_text_url(url):
    #ff1.1
    try:
        good_response = requests.get(url, timeout=(5,10))
        good_response.raise_for_status()
        return good_response.text
    except requests.RequestException as e:
        return "Error!please try again:" + str(e)

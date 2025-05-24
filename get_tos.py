#L1
import requests
#L2
from bs4 import BeautifulSoup
#L3
from urllib.parse import urljoin

TOS_PATH_NAMES = ["/terms","/terms-of-service","/legal/terms","tos","/legal","/legal/user"]
#F1
def get_tos_url(main_url):
    for path in TOS_PATH_NAMES:
        #ff1.1
        test_all_names = urljoin(main_url,path)
        try:
            good_response = requests.get(test_all_names,timeout=(5,10))
        except requests.RequestException:
            continue
        if good_response.ok and "terms" in good_response.text.lower():
            return test_all_names
    return None
#F2
def get_text_url(url):
    #ff2.1
    try:
        good_response = requests.get(url, timeout=(5,10))
        soup = BeautifulSoup(good_response.text,'html.parser')
        paragraphs = soup.find_all(["p","li"])
        texts = []
        for tag in paragraphs:
            texts.append(tag.get_text())
        text = ' '.join(texts)
        return text.strip()
    except Exception as e:
        return "Error!please try again:" + str(e)
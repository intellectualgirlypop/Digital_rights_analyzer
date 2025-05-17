"""
Author: Trinity Wilson 
Email: Intellectualgirlypop@gmail.com
Date started: 5/16/25
"""
#L1
import requests
#L2
from bs4 import BeautifulSoup
#L3
from urllib.parse import urljoin

TOS_PATH_NAMES = ["/terms","/terms-of-service","/legal/terms","tos"]
#F1
def get_tos_url(main_url):
    for path in TOS_PATH_NAMES:
        #ff1
        test_all_names = urljoin(main_url,path)
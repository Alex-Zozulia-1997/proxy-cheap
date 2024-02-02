# you can whitelist your IP in the dashboard
import requests

# Proxy server URL without username and password
proxy = "http://213.178.141.197:46007"

# Setup proxies dictionary without authentication
proxies = {
    "http": proxy,
    "https": proxy,
}

# Target URL
url = "https://ipv4.icanhazip.com"

# Making the GET request through the proxy
response = requests.get(url, proxies=proxies)

# Printing the response text (should be the IP address provided by the proxy)
print(response.text)

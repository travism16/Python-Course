import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
import os
import json
# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

ip_addr = input("Create an IP Address: ")
ip_addr = f"{ip_addr}/32"

if __name__ == "__main__":
    
    url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"
    
    post_data = {"address": ip_addr}

    response = requests.post(url, headers=http_headers, data=json.dumps(post_data), verify=False)
    response = response.json()
 
    print()
    pprint(response)
    print()

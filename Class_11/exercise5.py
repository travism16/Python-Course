import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
import os
import json
# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

ip_id = input("Enter IP Address ID: ")
ip_desc = input("Enter a description: ")
    
if __name__ == "__main__":
    
    url = f"https://netbox.lasthop.io/api/ipam/ip-addresses/{ip_id}/"
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"
    http_headers["Content-Type"] = "application/json; version=2.4;"

    # Get address from address id
    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()
    ip_addr = response['address']

    post_data = {"address": ip_addr, "description": ip_desc}

    response = requests.put(
        url,
        headers=http_headers,
        data=json.dumps(post_data),
        verify=False
    )
 
    print()
    print(f"Status code: {response.status_code}")
    print()
    print(f"JSON: ")
    pprint(response.json())
    print()

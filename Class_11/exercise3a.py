import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
import os
# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    
if __name__ == "__main__":
    
    url = "https://netbox.lasthop.io/api/dcim/devices"
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"
    response = requests.get(url, headers=http_headers, verify=False)
    devices = response.json()
    devices = devices["results"]

    print("\nDevice List:\n", ("-" * 10))
    
    for device in devices:
        print(device["display_name"])

    print()

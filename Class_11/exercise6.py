import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
import os
import sys
import json
# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

ip_id = input("Enter IP Address ID: ")
    
if __name__ == "__main__":
    
    url = f"https://netbox.lasthop.io/api/ipam/ip-addresses/{ip_id}/"
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"
    http_headers["Content-Type"] = "application/json; version=2.4;"

    # Try to get address from address id
    try:
        response = requests.get(url, headers=http_headers, verify=False)
        response = response.json()
        ip_addr = response['address']
    except:
        print("\nAddress not found!\n")
        sys.exit(1)

    # Delete address object
    response = requests.delete(
        url,
        headers=http_headers,
        verify=False
    )
    print(f"IP Address {ip_addr} deleted successfully!")
    print(f"Status Code: {response.status_code}\n") 

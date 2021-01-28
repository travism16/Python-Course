import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    
if __name__ == "__main__":
    
    url = "https://netbox.lasthop.io/api/"
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    response = requests.get(url, headers=http_headers, verify=False)
    
    print("\nStatus Code:")
    pprint(response.status_code)
    print("\nText:")
    pprint(response.text)
    print("\nJSON:")
    pprint(response.json())
    print("\nHeaders:")
    pprint(response.headers)
    print()

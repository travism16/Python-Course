import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    
if __name__ == "__main__":
    
    url = "https://netbox.lasthop.io/api/"
    response = requests.get(url, verify=False)
    print("\nStatus Code:")
    pprint(response.status_code)
    print("\nText:")
    pprint(response.text)
    print("\nJSON:")
    pprint(response.json())
    print("\nHeaders:")
    pprint(response.headers)
    print()

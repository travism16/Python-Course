import json
import pprint

filename = "json_arp_data.json"
with open(filename) as (f):
        json_data = json.load(f)

mac_dict = {}

for entry in json_data.items():
	hw_address = entry["hwAddress"]
	ip_addr = entry["address"]
	mac_dict[ip_addr] = hw_address

print(mac_dict)


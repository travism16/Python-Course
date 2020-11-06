import json
from pprint import pprint

with open('napalm.json') as f:
	json_data = json.load(f)


pprint(json_data)

ipv4 = []
ipv6 = []

#for interface, ip_protocol in json_data.items():
#     for ipv4_ipv6, addr_info in ip_protocol.items():
#         for ipaddr, prefix_info in addr_info.item():


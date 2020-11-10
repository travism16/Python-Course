import json
from pprint import pprint

with open('napalm.json') as f:
	json_data = json.load(f)

ipv4 = []
ipv6 = []

for interface, ip_protocol in json_data.items():
    for ipv4_ipv6, addr_info in ip_protocol.items():
        for ipaddr, prefix_info in addr_info.items():
            prefix_ln = prefix_info["prefix_length"]
            if ipv4_ipv6 == "ipv4":
                ipv4.append("{}/{}".format(ipaddr, prefix_ln))
            elif ipv4_ipv6 == "ipv6":
                ipv6.append("{}/{}".format(ipaddr, prefix_ln))

print()
print("IPv4 Addresses and prefix: ")
pprint(ipv4)
print()
print("IPv6 Addresses and prefix: ")
pprint(ipv6)
print()

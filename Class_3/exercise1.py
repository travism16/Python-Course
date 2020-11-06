import re
from pprint import pprint

arp_table = list(open('arp_table.txt', 'r').read().strip().splitlines())

arp_list = []
for arp_entry in arp_table:
	if re.search(r"^Protocol.*Interface$", arp_entry):
		continue
	_, ip_addr, _, mac_addr, _, intf = arp_entry.split()
	arp_dict = {"mac_addr": mac_addr, "ip_addr": ip_addr, "intf": intf}
	arp_list.append(arp_dict)

print()
pprint(arp_list)
print()

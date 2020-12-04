import xmltodict
from pprint import pprint

filename = open("show_security_zones.xml")
xml_data = filename.read().strip()
xml_parsed = xmltodict.parse(xml_data)

# Exercise 2a
print()
print("=" * 40)
print("Exercise 2a")
print("-" * 10)
print("Type: ", type(xml_parsed))
print()
pprint(xml_parsed)

# Exercise 2b
print()
print("=" * 40)
print("Exercise 2b")
print("-" * 10)
zones = xml_parsed["zones-information"]["zones-security"]
for index, zone in enumerate(zones, 1):
    print(f"Security Zone #{index}: {zone['zones-security-zonename']}")
print()

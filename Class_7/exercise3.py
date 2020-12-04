import xmltodict
from pprint import pprint

# Exercise 3a func
def xmlparser(filename):
    with open(filename) as f:
        return xmltodict.parse(f.read())

# Exercise 3c func
def xmlparserforce(filename, force_list=None):
    if force_list == None:
        force_list = {}
    with open(filename) as f:
        return xmltodict.parse(f.read(), force_list=force_list)

# Exercise 3a
print("=" * 40)
print("Exercise 3a")
print("-" * 12)
print()
security_zones = xmlparser("show_security_zones.xml")
security_zones_trust = xmlparser("show_security_zones_trust.xml")
pprint(security_zones)
print()
pprint(security_zones_trust)

# Exercise 3b
print("=" * 40)
print("Exercise 3b")
print("-" * 12)
print()
print("Type of show_security_zones.xml: ", end="")
print(type(security_zones["zones-information"]["zones-security"]))
print()
print("Type of show_security_zones_trust.xml: ", end="")
print(type(security_zones_trust["zones-information"]["zones-security"]))
print()

# Exercise 3c
print("=" * 40)
print("Exercise 3c")
print("-" * 12)
print()
filename = "show_security_zones_trust.xml"
security_zones_trust = xmlparserforce(filename, force_list={"zones-security": True})
print("Type of show_security_zones_trust.xml after parsing to list: ", end="")
print(type(security_zones_trust["zones-information"]["zones-security"]))
print()

from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

srx2_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
srx2_device.open()
srx2_device.timeout = 60

# Exercise 1a
print()
pprint(srx2_device.facts)
print("\n\n")
print("#" * 24)
print("Hostname: " + srx2_device.facts['hostname'])
print("#" * 24)
print()

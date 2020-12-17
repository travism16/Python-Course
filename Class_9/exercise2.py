from my_devices import all_devices
from my_functions import napalm_conn, create_backup
from pprint import pprint

napalm_objects = []

for device in all_devices:
    napalm_objects.append(napalm_conn(device))

# Exercise 2b
for device in napalm_objects:
    hostname = device.hostname
    print("\n")
    print(f"{hostname}'s ARP Table:")
    print("-" * 40)
    pprint(device.get_arp_table())

print("=" * 40)

# Exercise 2b
for device in napalm_objects:
    hostname = device.hostname
    print()
    print(f"NTP Peers of {hostname}: ")
    try:
        output = device.get_ntp_peers()
        print(output)
    except:
        print("Unable to gather NTP peers!")

print("=" * 40)

# Exercise 2c
for device in napalm_objects:
    print(f"Creating backup for {device.hostname}...")
    create_backup(device)

print()

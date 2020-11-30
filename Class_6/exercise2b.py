import pyeapi
from getpass import getpass
from my_funcs import yaml_loader, print_arp

# Import YAML device list into device_list
device_list = yaml_loader()

# Get password input
password = getpass()

# Add password to device dictionary and setup connection
# Grabs output of sh ip arp and grabs IP and MACs, then print
for device_name, device_dict in device_list.items():
    device_dict['password'] = password
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable("show ip arp")
    arp_list = output[0]['result']['ipV4Neighbors']
    print_arp(arp_list)


import pyeapi
from getpass import getpass
import yaml

# Import YAML device list
file = "arista_devices.yml"
with open(file) as f:
    device_list = yaml.load(f)

# Get password input
password = getpass()

# Create header for arp list
print("IP Address   --   MAC Address")
print("=" * 40)

# Add password to device dictionary and setup connection
# Grabs output of sh ip arp and grabs IP and MACs, then print
for device_name, device_dict in device_list.items():
    device_dict['password'] = password
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable("show ip arp")
    arp_list = output[0]['result']['ipV4Neighbors']

    for client in arp_list:
        print(client['address'] + "  --  " + client['hwAddress'])


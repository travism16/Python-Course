import pyeapi
from getpass import getpass
from my_funcs import yaml_loader, print_arp

# Import YAML device list into device_list
device_list = yaml_loader()

# Get password input
password = getpass()

print()

# Add password to device dictionary and setup connection
# Grab route info from "show ip route"
for device_name, device_dict in device_list.items():
    device_dict['password'] = password
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable("show ip route")
    route_list = output[0]['result']['vrfs']['default']['routes']
    
    # Print route info
    for route, route_dict in route_list.items():
        route_type = route_dict['routeType']
        print("-" * 40)
        if route_type == "static":
            next_hop = route_dict['vias'][0]['nexthopAddr']
            print("Route: " + route)
            print("Type: " + route_type)
            print("Next Hop: " + next_hop)
        else:
            print("Route: " + route)
            print("Type: " + route_type)

print("-" * 40)

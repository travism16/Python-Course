from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from pprint import pprint
# import srx2 from device dictionary
from juniper_devices import srx2

# Exercise 2a
my_device = Device(**srx2)
my_device.open()
my_device.timeout = 60

# Exercise 2b
def check_connected(device):
    if device.connected is True:
        print("Connection established to {}".format(device.hostname))
    else:
        print("Failed to connect!")
        raise SystemExit

def gather_routes(device):
    routes = RouteTable(device)
    routes.get()
    return routes

def gather_arp(device):
    arp = ArpTable(device)
    arp.get()
    return arp

def print_output(device, routes, arp):
    device_dict = {}
    device_dict["hostname"] = device.hostname
    device_dict["port"] = device.port
    device_dict["user"] = device.user
    device_dict["routes"] = routes.items()
    device_dict["arp"] = arp.items()
    print("Hostname: ", device_dict['hostname'])
    print("Port: ", str(device_dict['port']))
    print("User: ", device_dict['user'])
    print("\nRouting Table:")
    pprint(device_dict['routes'])
    print("\nARP Table: ")
    pprint(device_dict['arp'])

print()
check_connected(my_device)
print()

routes = gather_routes(my_device)
arp = gather_arp(my_device)

print_output(my_device, routes, arp)


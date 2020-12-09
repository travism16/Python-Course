import sys
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from juniper_devices import srx2
from exercise2 import check_connected, gather_routes

# Functions
def configure_from_file(filename, device):
    print(f"Configuring {device.hostname} with '{filename}'... ", end="")
    cfg = Config(device)
    cfg.lock()
    cfgpath = filename
    cfg.load(path=filename, format="text", merge=True)
    cfg.commit()
    cfg.unlock()
    print("Done.\n")
    
def compare_routes(first_routes, second_routes):
    new_routes = []
    for route in second_routes.keys():
        if route not in first_routes.keys():
            new_routes.append(route)
    return new_routes

def delete_routes(device):
    print("Deleting added routes... \n")
    cfg = Config(device)
    cfg.lock()
    cfg.load("delete routing-options static route 203.0.113.16/32", format="set", merge=True)
    cfg.load("delete routing-options static route 203.0.113.161/32", format="set", merge=True)
    cfg.commit()
    cfg.unlock()

# Program start
if __name__ == "__main__":
    
    my_device = Device(**srx2)
    my_device.open()
    my_device.timeout = 60
    print()
    check_connected(my_device)
    print()

    # Exercise 4a
    first_routes = gather_routes(my_device)

    # Exercise 4b
    configure_from_file("route_add.conf", my_device)

    # Exercise 4c
    second_routes = gather_routes(my_device)
    print("These new routes were added:")
    print(compare_routes(first_routes, second_routes))
    print()

    # Exercise 4d
    delete_routes(my_device)

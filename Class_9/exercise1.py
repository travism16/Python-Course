from my_devices import all_devices
from napalm import get_network_driver
from pprint import pprint

def napalm_conn(device_obj):
    device_type = device_obj.pop("device_type")
    driver = get_network_driver(device_type)
    device_conn = driver(**device_obj)
    device_conn.open()
    return device_conn


if __name__ == "__main__":

    napalm_objects = []

    for device in all_devices:
        napalm_objects.append(napalm_conn(device))
    
    print("=" * 40)

    for device in napalm_objects:
        print("Napalm object: ", device)
        print("-" * 36)
        print("Platform: ", device.platform)
        print("-" * 32)
        print("Get Facts: \n")
        pprint(device.get_facts())
        print()
        print("=" * 40)

    print()

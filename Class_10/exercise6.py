from my_functions import ssh_command2
from my_devices import devices_list
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime

start_time = datetime.now()
max_procs = 5

cmd_list = []
for device in devices_list:
    if device["device_type"] == "juniper_junos":
        cmd_list.append("show arp")
    else:
        cmd_list.append("show ip arp")

with ProcessPoolExecutor(max_procs) as pool:
    results = pool.map(ssh_command2, devices_list, cmd_list)
    for result in results:
        print("=" * 40)
        print(result)
        end_time = datetime.now()
        print("\nElasped time: ", end_time - start_time)

print("=" * 40)

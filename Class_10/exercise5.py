from my_functions import ssh_command2
from my_devices import devices_list
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime

start_time = datetime.now()
max_procs = 5
pool = ProcessPoolExecutor(max_procs)

with ProcessPoolExecutor(max_procs) as pool:
    future_list = []

    for device in devices_list:
        future = pool.submit(ssh_command2, device, "show version")
        future_list.append(future)

    for future in as_completed(future_list):
        print("=" * 40)
        print(future.result())
        end_time = datetime.now()
        print("\nElapsed time: ", end_time - start_time)
        print()

print("=" * 40)


from my_functions import ssh_command2
from my_devices import devices_list
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

start_time = datetime.now()
max_threads = 5
pool = ThreadPoolExecutor(max_threads)

future_list = []

for device in devices_list:
    future = pool.submit(ssh_command2, device, "show version")
    future_list.append(future)

for future in as_completed(future_list):
    print("=" * 40)
    print(future.result())

end_time = datetime.now()
print("=" * 40)
print("\nElapsed time: ", end_time - start_time)
print()


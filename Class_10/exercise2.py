from my_functions import ssh_command
from my_devices import devices_list
from datetime import datetime
import threading

start_time = datetime.now()


for device in devices_list:
    thread = threading.Thread(target=ssh_command, args=(device, "show version"))
    thread.start()

main_thread = threading.currentThread()

for thread in threading.enumerate():
    if thread != main_thread:
        thread.join()

print("\nElapsed time: " + str(datetime.now() - start_time))

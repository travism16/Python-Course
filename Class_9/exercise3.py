from my_devices import cisco3, arista1
from my_functions import napalm_conn, create_backup
from pprint import pprint

#napalm_objects = []

#for device in all_devices:
#    napalm_objects.append(napalm_conn(device))

cisco3_conn = napalm_conn(cisco3)
arista1_conn = napalm_conn(arista1)

# Exercise 3b
cisco3_filename = "cisco3.lasthop.io-loopbacks.txt"
arista1_filename = "arista1.lasthop.io-loopbacks.txt"

print("Loading configs...")
cisco3_conn.load_merge_candidate(filename=cisco3_filename)
arista1_conn.load_merge_candidate(filename=arista1_filename)

# Exercise 3c
print()
print("cisco3.lasthop.io config diff:")
print("-" * 40)
print(cisco3_conn.compare_config())
print()
print("arista1.lasthop.io config diff:")
print("-" * 40)
print(arista1_conn.compare_config())
print()

# Exercise 3d 
print("Committing config...")
cisco3_conn.commit_config()
arista1_conn.commit_config()

print()
print("cisco3.lasthop.io config diff:")
print("-" * 40)
print(cisco3_conn.compare_config())
print()
print("arista1.lasthop.io config diff:")
print("-" * 40)
print(arista1_conn.compare_config())
print()


from my_devices import nxos1
from my_functions import napalm_conn, create_checkpoint

nxos1_conn = napalm_conn(nxos1)

# Exercise 4a
print()
print("Creating checkpoint for nxos1...")
create_checkpoint(nxos1_conn)

# Exercise 4d
print()
print("Loading candidate config...")
nxos1_conn.load_replace_candidate(filename="nxos1.lasthop.io-checkpoint-NEW.txt")
print()
print("Compare diff with new config loaded:\n", "-" * 32)
print(nxos1_conn.compare_config())
print("-" * 32, "\n")
print("Discarding changes...")
nxos1_conn.discard_config()
print()

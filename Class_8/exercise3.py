from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError
from pprint import pprint
from juniper_devices import srx2
from exercise2.py import check_connected

my_device = Device(**srx2)
my_device.open()
my_device.timeout = 60

check_connected(my_device)

cfg = Config(my_device)

# Exercise 3a
cfg.lock()

try:
    cfg.lock()
except LockError:
    print("Config already locked!")

# Exercise 3b
cfg.load("set system host-name Router-Man-5000", format="set", merge=True)

# Exercise 3c
print()
print(cfg.diff())
print()

# Exercise 3d
cfg.rollback(0)
print("Rolling back config...")
print()
print(cfg.diff())
print()

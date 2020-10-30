import os
import time
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

net_connect = ConnectHandler(**device)

output = net_connect.find_prompt()
print(output)

net_connect.config_mode()
output = net_connect.find_prompt()
print(output)

net_connect.exit_config_mode()
output = net_connect.find_prompt()
print(output)

net_connect.write_channel("disable\n")
output = net_connect.find_prompt()
print(output)
time.sleep(2)
output = net_connect.read_channel()
print(output)
net_connect.enable()
output = net_connect.find_prompt()
print(output)


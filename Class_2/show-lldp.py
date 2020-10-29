import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
	"host": "nxos1.lasthop.io",
	"username": "pyclass",
	"password": getpass(),
	"device_type": "cisco_nxos",
	"session_log": "nxos1_session.txt", 
	"global_delay_factor": 2
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command("show lldp neighbors", strip_prompt=False, strip_command=False)

now = datetime.now()
time = now.strftime("%m/%d/%Y, %H:%M:%S")

print()
print(output)
print("Command was successfully executed at ", time) 
print(("=")*55)
print()

output = net_connect.send_command("show lldp neighbors", delay_factor=8, strip_prompt=False, strip_command=False)

now = datetime.now()
time = now.strftime("%m/%d/%Y, %H:%M:%S")

print()
print(output)
print("Command was successfully executed at ", time,"!")
print(("=")*55)
print()


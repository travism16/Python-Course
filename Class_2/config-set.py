import os
from netmiko import ConnectHandler
from getpass import getpass

device = {
	"host": "cisco3.lasthop.io",
	"username": "pyclass",
	"password": getpass(),
	"device_type": "cisco_ios",
	#"session_log": "cisco3_session.txt", 
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

commands = [
	'ip name-server 1.1.1.1',
	'ip name-server 1.0.0.1',
	'ip domain-lookup',
]

output = net_connect.send_config_set(commands, strip_prompt=False, strip_command=False)

print()
print(output)

output = net_connect.send_command("ping google.com", strip_prompt=False, strip_command=False)

print()
print(output)

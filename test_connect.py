import os
from netmiko import ConnectHandler
from getpass import getpass


cisco3 = {
	"host": "cisco3.lasthop.io",
	"username": "pyclass",
	"password": getpass(),
	"device_type": "cisco_ios",
	#"session_log": "cisco3_session.txt" 
}

cisco4 = {
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_ios",
        #"session_log": "cisco4_session.txt"
}

command = "sh ip int brief"

for device in (cisco3, cisco4):
	net_connect = ConnectHandler(**device)
	print(net_connect.find_prompt())
	print(net_connect.send_command(command))
	print("-" * 50)

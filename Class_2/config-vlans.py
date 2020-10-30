import os
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
	"host": "nxos1.lasthop.io",
	"username": "pyclass",
	"password": getpass(),
	"device_type": "cisco_nxos",
	#"session_log": "nxos1_session.txt", 
}

device2 = {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_nxos",
        #"session_log": "nxos2_session.txt",
}


net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_config_from_file(config_file="vlans.txt", strip_prompt=False, strip_command=False)
output += net_connect.save_config()
print()
print(output)
print()

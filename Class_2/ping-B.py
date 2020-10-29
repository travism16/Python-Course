import os
from netmiko import ConnectHandler
from getpass import getpass


device = {
	"host": "cisco4.lasthop.io",
	"username": "pyclass",
	"password": getpass(),
	"device_type": "cisco_ios",
	"session_log": "cisco4_session.txt" 
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command("ping", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("8.8.8.8\n", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)

print(output)

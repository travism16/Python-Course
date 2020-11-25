from netmiko import ConnectHandler
from getpass import getpass


cisco3 = {
	"host": "cisco3.lasthop.io",
	"username": "pyclass",
	"password": getpass(),
	"device_type": "cisco_ios",
	"session_log": "cisco3_session.txt" 
}

command = "sh run"

net_connect = ConnectHandler(**cisco3)

net_connect.send_command(command)
net_connect.disconnect()

import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device = {
	"host": "cisco4.lasthop.io",
	"username": "pyclass",
	"password": getpass(),
	"device_type": "cisco_ios",
	"session_log": "cisco4_session.txt"
}

net_connect = ConnectHandler(**device)


output = net_connect.send_command("show version", use_textfsm=True)

#pprint(output)
#print()
#print(("*")*55)

output = net_connect.send_command("show lldp neighbors", use_textfsm=True)

#pprint(output)
#print()
#print(("*")*55)
#print()

neighbor = output[0]['neighbor']
output = output[0]['neighbor_interface'] 
print("LLDP Neighbor ", neighbor, " interface is port ", output)

net_connect.disconnect()

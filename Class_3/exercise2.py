import yaml
device_list = [
{"device_name": 'Cisco3', "hostname": 'cisco3.lasthop.io', "username": 'admin', "password": 'secret123'},
{"device_name": 'Cisco4', "hostname": 'cisco4.lasthop.io', "username": 'admin', "password": 'secret123'},
{"device_name": 'Arista1', "hostname": 'arista1.lasthop.io', "username": 'admin', "password": 'password321'},
{"device_name": 'Arista2', "hostname": 'arista2.lasthop.io', "username": 'admin', "password": 'password321'}
]

filename = "device_list.yaml"

with open(filename, "wt") as f:
	yaml.dump(device_list, f)


from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler

# Create Jinja2 environment and set template folders
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.','./templates'])

# Variables passed to J2
nxos1_vars = {
    "hostname": "nxos1.lasthop.io",
    "interface": "Ethernet1/2",
    "ip_addr": "10.1.111.1",
    "netmask": "/24",
    "local_as": 22
}

nxos2_vars = {
    "hostname": "nxos2.lasthop.io",
    "interface": "Ethernet1/2",
    "ip_addr": "10.1.111.2",
    "netmask": "/24",
    "local_as": 22
}

nxos1_vars["peer_ip"] = nxos2_vars["ip_addr"]
nxos2_vars["peer_ip"] = nxos1_vars["ip_addr"]

# Import device list - will ask for password, then create list
from my_devices import nxos1, nxos2
device_list = [nxos1, nxos2]
nxos1["j2_vars"] = nxos1_vars
nxos2["j2_vars"] = nxos2_vars

# Process devices with J2, create temp_device to keep J2_vars on original device element
for device in (nxos1, nxos2):
    template_file = "int_conf.j2"
    template = env.get_template(template_file)
    temp_device = device.copy()
    j2_vars = {}
    j2_vars = temp_device.pop("j2_vars")
    commands = template.render(**j2_vars) 
    print("=" * 40)
    print()
    print(f"Configure device {device['host']} with these commands:")
    print()
    print(commands)
    print()
    print("=" * 40)
    print()
    # Create list of commands
    command_lines = commands.splitlines()
    # Use netmiko to connect to device and enter commands
    net_connect = ConnectHandler(**temp_device)
    output = net_connect.send_config_set(command_lines)
    print("***OUTPUT FROM CONNECT HANDLER***")
    print()
    print(output)
    print()

# Seperator lines for testing output
print()
print('=' * 40)
print("Performing tests on devices...")
print('=' * 40)
print()

# Verify results
for device in (nxos1, nxos2):
    remote_ip = device['j2_vars']['peer_ip']
    del device['j2_vars']
    net_connect = ConnectHandler(**device)
    prompt = net_connect.find_prompt()
    output = net_connect.send_command(f"ping {remote_ip}")
    print(device['host'])
    print("Pinging remote peer...")
    print()
    print(prompt)
    print(output)
    print()
    print('=' * 40)
    print()




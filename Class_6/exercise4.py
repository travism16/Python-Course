from getpass import getpass
from jinja2.environment import Environment
from jinja2 import FileSystemLoader, StrictUndefined
from my_funcs import yaml_loader
import pyeapi
import yaml

# Set environment and set Jinja2 template file
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')
template_file = "ip_int_config.j2"

# Function for loading devices with YAML file
#def yaml_loader(file = "arista_devices_all.yml"):
#    with open(file) as f:
#        return yaml.safe_load(f)
#    raise ValueError("Readin YAML file failed")

device_list = yaml_loader(file = "arista_devices_all.yml")

# Get password input
password = getpass()

print()

# Add password to device dictionary and setup connection
# Grab route info from "show ip route"
for device_name, device_dict in device_list.items():
    device_dict['password'] = password
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    
    # Create config template
    template = env.get_template(template_file)
    j2_vars = device_dict['data']
    intf_config = template.render(**j2_vars)
    intf_config = intf_config.strip()
    intf_config = intf_config.splitlines()

    # Send device configuration and verify with show command
    output = device.config(intf_config)
    output = device.enable("show ip interface brief")
    print(device_name)
    print("-" * 10)
    print(output[0]['result']['output'].rstrip())
    print("=" * 40)

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
import re

# Setup Jinja2 environment and template folders
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.','./templates'])

# Set variables for temlate
device_vars = {"vrf_name": "blue", "rd_number": "100:1", "ipv4_enabled": "yes", "ipv6_enabled": "yes"}

template_file = "vrf.j2"
template = env.get_template(template_file)
commands = template.render(**device_vars)
print()
print(commands)

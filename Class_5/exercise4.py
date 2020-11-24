from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
import re

# Setup Jinja2 environment and template folders
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.','./templates'])

# Set variables for temlate
device_vars = [
    {"vrf_name": "blue", "rd_number": "100:1", "ipv4_enabled": "yes", "ipv6_enabled": "yes"},
    {"vrf_name": "red", "rd_number": "200:1", "ipv4_enabled": "yes", "ipv6_enabled": "yes"},
    {"vrf_name": "green", "rd_number": "300:1", "ipv4_enabled": "yes", "ipv6_enabled": "yes"},
    {"vrf_name": "black", "rd_number": "400:1", "ipv4_enabled": "yes", "ipv6_enabled": "yes"},
    {"vrf_name": "white", "rd_number": "500:1", "ipv4_enabled": "yes", "ipv6_enabled": "yes"}
]

for device in device_vars:
    template_file = "vrf.j2"
    template = env.get_template(template_file)
    commands = template.render(**device)
    print()
    print(commands)
    print("-" * 40)


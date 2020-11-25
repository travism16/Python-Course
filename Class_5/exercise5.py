from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler

# Setup Jinja2 environment and template folders
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.','./templates'])

# Set variables for temlate
cisco3_vars = {
        'ntp1': '130.126.24.24',
        'ntp2': '152.2.21.1',
        'timezone': 'PST',
        'timezone_offset': '-8',
        'timezone_dst': 'PDT'
}

template_file = "cisco3_config.j2"
template = env.get_template(template_file)
commands = template.render(**cisco3_vars)
print()
print(commands)
print("-" * 40)


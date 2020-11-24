from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.','./templates'])

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "interface": "Ethernet1/2",
    "ip_addr": "10.1.100.1",
    "netmask": "/24",
    "local_as": 22
}

nxos2 = {
    "hostname": "nxos2.lasthop.io",
    "interface": "Ethernet1/1",
    "ip_addr": "10.1.100.2",
    "netmask": "/24",
    "local_as": 22
}

nxos1["peer_ip"] = nxos2["ip_addr"]
nxos2["peer_ip"] = nxos1["ip_addr"]

for device in (nxos1, nxos2):
    print(f"{device['hostname']}")
    template_file = "int_conf.j2"
    template = env.get_template(template_file)
    output = template.render(**device)
    print()
    print(output)
    print()

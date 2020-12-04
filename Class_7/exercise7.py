from nxapi_plumbing import Device
from lxml import etree
from getpass import getpass

nxos1 = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False
)

output = nxos1.show("show interface Ethernet1/1")

# Exercise 7a
print(
    "Interface: {}; State: {}; MTU: {}".format(
        output.find(".//interface").text,
        output.find(".//state").text,
        output.find(".//eth_mtu").text,
    )
)

# Exercise 7b
cmds = ["show system uptime", "show system resources"]
output = nxos1.show_list(cmds)
for entry in output:
    print(etree.tostring(entry).decode())

# Exercise 7c

cfg_cmds = [
    "interface Loopback120",
    "description My loopback",
    "interface Loopback121",
    "description My loopback again"
]

output = nxos1.config_list(cfg_cmds)

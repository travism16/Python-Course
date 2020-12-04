from nxapi_plumbing import Device
from getpass import getpass

nxos1 = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False
)

output = nxos1.show("show interface Ethernet1/1")
if_name = output["TABLE_interface"]["ROW_interface"]["interface"]
if_state = output["TABLE_interface"]["ROW_interface"]["state"]
if_mtu = output["TABLE_interface"]["ROW_interface"]["eth_mtu"]

print()
print(f"Interface: {if_name}; State: {if_state}; MTU: {if_mtu}")
print()

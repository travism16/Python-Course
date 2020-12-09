import sys
from jnpr.junos import Device
from juniper_devices import srx2
from lxml import etree
from exercise2 import check_connected

if __name__ == "__main__":

    my_device = Device(**srx2)
    my_device.open()
    my_device.timeout = 60
    
    print()
    check_connected(my_device)
    print()

    # Exercise 5a
    print("Show Version XML:\n", "=" * 24, "\n")
    xml_out = my_device.rpc.get_software_information()
    print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))

    # Exercise 5b
    print("\n\nShow terse interface information:\n", "=" * 24, "\n")
    xml_out = my_device.rpc.get_interface_information(terse=True)
    print(etree.tostring(xml_out, encoding="unicode"))

    # Exercise 5c
    print("\n\nShow terse interface fe-0/0/7:\n", "=" * 24, "\n")
    xml_out = my_device.rpc.get_interface_information(
        interface_name="fe-0/0/7", terse=True, normalize=True
    )
    print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))

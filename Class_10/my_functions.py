from netmiko import ConnectHandler

def ssh_command(device, show_command):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(show_command)
    print("=" * 40)
    print(output)
    net_connect.disconnect()

def ssh_command2(device, show_command):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(show_command)
    return output
    net_connect.disconnect()


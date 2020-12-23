from netmiko import ConnectHandler
from datetime import datetime
from my_devices import devices_list

def ssh_conn(device, show_command):
    net_connect = ConnectHandler(**device)
    return net_connect.send_command(show_command)
    net_connect.disconnect()

if __name__ == "__main__":
    start_time = datetime.now()
    print("Start time: ", start_time)
    
    for device in devices_list:
        print("=" * 40)
        print(ssh_conn(device, "show version"))

    end_time = datetime.now()
    print("=" * 40)
    print("\nStart Time: ", start_time)
    print("End Time: ", end_time)
    

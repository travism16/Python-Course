from napalm import get_network_driver

def napalm_conn(device_obj):
    device_type = device_obj.pop("device_type")
    driver = get_network_driver(device_type)
    device_conn = driver(**device_obj)
    device_conn.open()
    return device_conn

def create_backup(device):
    get_run = device.get_config()
    run_conf = get_run['running']
    filename = f"{device.hostname}-running-config.txt"
    with open(filename, "w") as f:
        f.write(run_conf)

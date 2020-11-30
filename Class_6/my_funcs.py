import yaml

def yaml_loader():
    file = "arista_devices.yml"
    with open(file) as f:
        return yaml.safe_load(f)
    raise ValueError("Readin YAML file failed")

def print_arp(arp_list):
    print("IP Address   --   MAC Address")
    print("=" * 40)
    
    for client in arp_list:
        print(client['address'] + "  --  " + client['hwAddress'])

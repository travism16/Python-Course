import yaml
from netmiko import ConnectHandler

#not uploaded to Github
file = ".netmiko.yml"

with open(file) as f:
    my_data = yaml.load(f)

cisco3 = my_data['cisco3']
netcon = ConnectHandler(**cisco3)

print(netcon.find_prompt())

import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

#not uploaded to Github
file = ".netmiko.yml"

with open(file) as f:
    my_data = yaml.load(f)

cisco4 = my_data['cisco4']
netcon = ConnectHandler(**cisco4)
sh_run = netcon.send_command("sh run")
my_config = netcon.send_command("sh run ")
my_config = CiscoConfParse(sh_run.splitlines())

ip_int = my_config.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip addres")

for int in ip_int:
    print()
    print(int.text)
    ip_address = int.re_search_children(r"ip address")[0].text
    print(ip_address)
    print()


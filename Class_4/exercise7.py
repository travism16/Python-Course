import textfsm
from pprint import pprint

template_file = "ex2_show_int_status.tpl"
template = open(template_file)

with open("ex2_show_int_status.txt") as f:
    raw_text = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text)
template.close()

dict_keys = re_table.header
int_status_list = []

for textfsm_list in data:
    textfsm_dict = dict(zip(dict_keys, textfsm_list))
    int_status_list.append(textfsm_dict)

print()
pprint(int_status_list)
print()

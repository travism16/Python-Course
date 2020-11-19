import textfsm
from pprint import pprint

template_file = "ex1_show_int_status.tpl"
template = open(template_file)

with open("ex1_show_int_status.txt") as f:
    raw_text = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text)

print()
pprint(data)
print()
template.close()

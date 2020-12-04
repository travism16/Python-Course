from lxml import etree

def xml_reader(filename):
    with open(filename, "rb") as f:
        return etree.fromstring(f.read())

### Exercise 5a
filename = "show_version.xml"
my_xml = xml_reader(filename)
print()
print(f"{filename} default name space: ")   # Exercise 5a
print(my_xml.nsmap)
print()
print("Board ID: " + my_xml.find(".//{*}proc_board_id").text)   # Exercise 5b
print()

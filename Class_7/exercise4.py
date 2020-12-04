from lxml import etree

with open("show_security_zones.xml") as f:
    my_xml = etree.fromstring(f.read())

### Exercise 4a
# Finds first instance of "zones-security" in xml file
first_sec_zone = my_xml.find("zones-security")

# Print first tag
print()
print("EXERCISE 4a\n" + ("=" * 12))
print()
print("Find tag of the first zones-security element")
print("-" * 20)
print(first_sec_zone.tag, end="\n\n")
# Print child tags
print("Find tag of all child elements of the first zones-security element")
print("-" * 20)
child_tags = []    # Create list for child tags
for child in first_sec_zone:    # Cycles through children nd adds their tag to list
    child_tags.append(child.tag)
for child in child_tags:
    print(child)
print()

### Exercise 4b
print("EXERCISE 4b\n" + ("=" * 12))
print()
print("First security zone name:")
print(first_sec_zone.find("zones-security-zonename").text)
print()

### Exercise 4c
print("EXERCISE 4c\n" + ("=" * 12))
print()
print("All zone security names:")
all_zone_sec = my_xml.findall("zones-security")
for zone in all_zone_sec:
    print(zone.find("zones-security-zonename").text)
print()

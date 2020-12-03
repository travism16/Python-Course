from lxml import etree

with open("show_security_zones.xml") as f:
    my_xml = etree.fromstring(f.read())

# Exercise 1a
print("=" * 40)
print("Exercise 1a output:")
print()
print(my_xml)
print(type(my_xml))
print()

# Exercise 1b
print("=" * 40)
print("Exercise 1b output:")
print()
print(etree.tostring(my_xml).decode())
print()

# Exercise 1c
print("=" * 40)
print("Exercise 1c output:")
print()
print("Root tag: " + my_xml.tag)
print("Children: ", end="")
print(len(my_xml.getchildren()))

# Exercise 1d
print("=" * 40)
print("Exercise 1d output:")
print()
print("First child: " + my_xml.getchildren()[0].tag)

# Exercise 1e
print("=" * 40)
print("Exercise 1e output:")
print()
trust_zone = my_xml.getchildren()[0]
print(etree.tostring(trust_zone).decode())

# Exercise 1f
print("=" * 40)
print("Exercise 1f output:")
print()
print("Child tags of Trust Zone:")
for child in trust_zone:
    print(child.tag)



# xml
# xml używa tagów

from xml.dom import minidom

root = minidom.Document()  # <?xml version="1.0" ?>
xml = root.createElement('root')
root.appendChild(xml)  # <root></root>

productChild = root.createElement('product')  # <product name="GFG"/>
productChild.setAttribute("name", "GFG")  # name="GFG
xml.appendChild(productChild)

xml_str = root.toprettyxml(indent="\t")
print(xml_str)

# <?xml version="1.0" ?>
# <root>
# 	<product name="GFG"/>
# </root>

save_path = 'gfg.xml'
with open(save_path, "w") as f:
    f.write(xml_str)

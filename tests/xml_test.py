import xml.etree.cElementTree as ET

annotation = ET.Element("annotation", verified="yes")

filename = 'boat-2.jpg'
ET.SubElement(annotation, "folder").text = "images"
ET.SubElement(annotation, "filename" ).text = filename

path = ET.SubElement(annotation, "path")
path.text = "/some/path/that/is/very/very/verylong.jpgskjakg"

source = ET.SubElement(annotation, "source")
ET.SubElement(source, "database").text = "Unknown"

size = ET.SubElement(annotation, "size")
ET.SubElement(size, "width").text = "800"
ET.SubElement(size, "height").text = "800"
ET.SubElement(size, "depth").text = "3"

segmented = ET.SubElement(annotation, 'segmented')
segmented.text = '0'

object = ET.SubElement(annotation, "object")
ET.SubElement(object, "name").text = "raccoon"
ET.SubElement(object, "pose").text = "Unspecified"
ET.SubElement(object, "truncated").text = "0"
ET.SubElement(object, "difficult").text = "0"

bndbox = ET.SubElement(object, "bndbox")
ET.SubElement(bndbox, "xmin").text = "50"
ET.SubElement(bndbox, "ymin").text = "51"
ET.SubElement(bndbox, "xmax").text = "150"
ET.SubElement(bndbox, "ymax").text = "151"


tree = ET.ElementTree(annotation)
tree.write("filename.xml")
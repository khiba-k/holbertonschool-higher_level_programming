import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to a file.

    Args:
    - dictionary (dict): Python dictionary to serialize.
    - filename (str): Filename to save the XML data.

    Returns:
    - None
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert value to string for XML serialization

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
    - filename (str): Filename from which to read XML data.

    Returns:
    - dict: Deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text  # Convert text back to appropriate Python type if needed

    return dictionary

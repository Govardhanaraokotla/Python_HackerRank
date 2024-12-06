def get_attr_number(node):
    # your code goes here
    return len(node.attrib) + sum(get_attr_number(i) for i in node);


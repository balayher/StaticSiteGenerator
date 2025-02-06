from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        delimited_nodes = old_node.text.split(delimiter)
        split_nodes = []
        if len(delimited_nodes) % 2 == 0:
            raise ValueError("Closing delimiter not found")
        for i in range(len(delimited_nodes)):
            if delimited_nodes[i] == "":
                continue
            if i % 2 == 0:
                to_add = TextNode(delimited_nodes[i], TextType.TEXT)
                split_nodes.append(to_add)
            else:
                to_add = TextNode(delimited_nodes[i], text_type)
                split_nodes.append(to_add)
        new_nodes.extend(split_nodes)
    return new_nodes
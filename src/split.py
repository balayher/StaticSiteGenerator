from textnode import TextNode, TextType
from extract import extract_markdown_images, extract_markdown_links

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

def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        iterating_node = old_node
        if len(images) == 0:
            new_nodes.append(iterating_node)
            continue
        for image in images:
            sections = iterating_node.text.split(f"![{image[0]}]({image[1]})", 1)
            iterating_node = TextNode(sections[1], TextType.TEXT)
            if len(sections) != 2:
                raise ValueError("Invalid: Image not closed")
            if sections[0] != "":
                to_add = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(to_add)
            to_add = TextNode(image[0], TextType.IMAGE, image[1])
            new_nodes.append(to_add)
        if iterating_node.text != "":
            new_nodes.append(iterating_node)
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        iterating_node = old_node
        if len(links) == 0:
            new_nodes.append(iterating_node)
            continue
        for link in links:
            sections = iterating_node.text.split(f"[{link[0]}]({link[1]})", 1)
            iterating_node = TextNode(sections[1], TextType.TEXT)
            if len(sections) != 2:
                raise ValueError("Invalid: Link not closed")
            if sections[0] != "":
                to_add = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(to_add)
            to_add = TextNode(link[0], TextType.LINK, link[1])
            new_nodes.append(to_add)
        if iterating_node.text != "":
            new_nodes.append(iterating_node)
    return new_nodes
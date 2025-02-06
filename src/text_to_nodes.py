from textnode import TextNode, TextType
from split import split_nodes_links, split_nodes_delimiter, split_nodes_images

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    node_list = split_nodes_delimiter([node], "**", TextType.BOLD)
    node_list = (split_nodes_delimiter(node_list, "*", TextType.ITALIC))
    node_list = (split_nodes_delimiter(node_list, "`", TextType.CODE))
    node_list = (split_nodes_images(node_list))
    node_list = (split_nodes_links(node_list))
    return node_list
 
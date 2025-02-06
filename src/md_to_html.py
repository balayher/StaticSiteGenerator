from blocks import block_to_block_type, markdown_to_blocks
from leafnode import LeafNode
from parentnode import ParentNode
from text_to_nodes import text_to_textnodes
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        node = block_to_htmlnode(block)
        nodes.append(node)
    return ParentNode("div", nodes)


def block_to_htmlnode(block):
    block_type = block_to_block_type(block)
    if block_type == "paragraph":
        return paragraph_to_htmlnode(block) 
    if block_type == "heading":
        return heading_to_htmlnode(block)
    if block_type == "code":
        return code_to_htmlnode(block)
    if block_type == "quote":
        return quote_to_htmlnode(block)
    if block_type == "unordered_list":
        return unordered_to_htmlnode(block)
    if block_type == "ordered_list":
        return ordered_to_htmlnode(block)
    raise ValueError("Invalid block type")
    
def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_htmlnode(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_htmlnode(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_htmlnode(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_to_htmlnode(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def unordered_to_htmlnode(block):
    lines = block.split("\n")
    html_lines = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_lines.append(ParentNode("li", children))
    return ParentNode("ul", html_lines)

def ordered_to_htmlnode(block):
    lines = block.split("\n")
    html_lines = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_lines.append(ParentNode("li", children))
    return ParentNode("ol", html_lines)
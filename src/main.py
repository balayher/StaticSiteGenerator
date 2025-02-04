from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    textnode = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
    htmldict = {
        "href": "https://www.google.com",
        "target": "_blank",  
    }
    htmlnode = HTMLNode("h1", "this be text", None, htmldict)
    print(textnode)
    html_test = htmlnode.props_to_html()
    print(html_test)
    leafnode = LeafNode("h1", "this be text", htmldict)
    print(leafnode)
    leaf_test = leafnode.to_html()
    print(leaf_test)

main()
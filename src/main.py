from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    textnode = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
    print(textnode)
    
main()
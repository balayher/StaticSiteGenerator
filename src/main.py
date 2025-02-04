from textnode import TextNode, TextType
from htmlnode import HTMLNode

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
   

main()
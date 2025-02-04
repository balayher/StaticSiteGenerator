import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        htmldict = {
            "href": "https://www.google.com",
            "target": "_blank",  
        }
        str_node = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(None, None, None, htmldict)
        node2 = node.props_to_html()
        self.assertEqual(str_node, node2)

        htmldict = {
            "href": "https://www.google.com", 
        }
        str_node = ' href="https://www.google.com"'
        node = HTMLNode(None, None, None, htmldict)
        node2 = node.props_to_html()
        self.assertEqual(str_node, node2)

        htmldict = {
            "hsrs": "https://www.google.com",
            "ams": "_blank",  
        }
        str_node = ''
        node = HTMLNode(None, None, None, None)
        node2 = node.props_to_html()
        self.assertEqual(str_node, node2)


        

if __name__ == "__main__":
    unittest.main()
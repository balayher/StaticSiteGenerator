import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        children = [
            LeafNode("b", "Bold text")
        ]

        str_node = '<p><b>Bold text</b></p>'
        node = ParentNode("p", children, None)
        node2 = node.to_html()
        self.assertEqual(str_node, node2)

        children = [
            LeafNode("b", "Bold text")
        ]
        htmldict = {
            "href": "https://www.google.com",  
        }
        str_node = '<a href="https://www.google.com"><b>Bold text</b></a>'
        node = ParentNode("a", children, htmldict)
        node2 = node.to_html()
        self.assertEqual(str_node, node2)

        children = [
            LeafNode("b", "Bold text"),
            LeafNode("a", "Link here", htmldict),
            LeafNode("i", "Italics!"),
        ]
        htmldict = {
            "href": "https://www.google.com",  
        }
        str_node = '<a href="https://www.google.com"><b>Bold text</b></a>'
        node = ParentNode("a", children, htmldict)
        node2 = node.to_html()
        self.assertNotEqual(str_node, node2)

        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "boring text here"),
            LeafNode("i", "Italics!"),
        ]
        adults = [
            ParentNode("p", children),
            LeafNode(None, "THE MIDDLE"),
            ParentNode("quo", children),
        ]
        htmldict = {
            "href": "https://www.google.com",  
        }
        str_node = '<a href="https://www.google.com"><b>Bold text</b></a>'
        node = ParentNode("a", adults, htmldict)
        node2 = node.to_html()
        self.assertNotEqual(str_node, node2)
 


        
if __name__ == "__main__":
    unittest.main()
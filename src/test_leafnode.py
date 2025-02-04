import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        htmldict = {
            "href": "https://www.google.com",
            "target": "_blank",  
        }
        str_node = 'test is here'
        node = LeafNode(None, "test is here", htmldict)
        node2 = node.to_html()
        self.assertEqual(str_node, node2)
        print(node2)

        htmldict = {
            "href": "https://www.google.com",
            "target": "_blank",  
        }
        str_node = '<p>test is here</p>'
        node = LeafNode("p", "test is here", None)
        node2 = node.to_html()
        self.assertEqual(str_node, node2)
        print(node2)

        htmldict = {
            "href": "https://www.google.com",
            "target": "_blank",  
        }
        str_node = '<a> test is here</a>'
        node = LeafNode("a", "test is here", htmldict)
        node2 = node.to_html()
        self.assertNotEqual(str_node, node2)
        print(node2)


        
if __name__ == "__main__":
    unittest.main()
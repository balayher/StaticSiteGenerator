import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.ITALIC, None)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

        node = TextNode("This is not a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", "TextType.BOLD", "https://www.boot.dev")
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2.tag, "b")
        self.assertEqual(node2.value, "This is a text node")

        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2.tag, None)
        self.assertEqual(node2.value, "This is a text node")

        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2.tag, "a")
        self.assertEqual(node2.value, "This is a text node")
        self.assertEqual(node2.props, {"href": "https://www.boot.dev"})

        node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
        node2 = text_node_to_html_node(node)
        self.assertEqual(node2.tag, "img")
        self.assertEqual(node2.value, "")
        self.assertEqual(node2.props, {"src": "https://www.boot.dev", "alt": "This is a text node"})


if __name__ == "__main__":
    unittest.main()
import unittest
from split import split_nodes_delimiter
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        test_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, test_nodes)

        node = TextNode("This is text with a **BOLD TEXT** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        test_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("BOLD TEXT", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, test_nodes)

        node = TextNode("This is *multiple* text with a *italics block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        test_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("multiple", TextType.ITALIC),
            TextNode(" text with a ", TextType.TEXT),
            TextNode("italics block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, test_nodes)

        node = TextNode("This is text with a `italics block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        test_nodes = [
            TextNode("This is text with a `italics block` word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, test_nodes)

        node = TextNode("This is **bold text** with a *italics* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        test_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" with a ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, test_nodes)

       
        

if __name__ == "__main__":
    unittest.main()
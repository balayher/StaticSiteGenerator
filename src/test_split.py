import unittest
from split import split_nodes_delimiter, split_nodes_links, split_nodes_images
from textnode import TextNode, TextType

class TestSplit(unittest.TestCase):
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

    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        test_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_nodes, test_nodes)

        node = TextNode(
            "This is text without a link",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        test_nodes = [
            TextNode("This is text without a link", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, test_nodes)

    def test_split_nodes_images(self):
        node = TextNode(
            "This is text with a image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        test_nodes = [
            TextNode("This is text with a image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_nodes, test_nodes)
       
        

if __name__ == "__main__":
    unittest.main()
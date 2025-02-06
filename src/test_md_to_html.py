import unittest
from md_to_html import markdown_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode


class TestMDtoHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        text = """
### Header

Paragraph

- List item one
- List item two
"""
        marked = markdown_to_html_node(text)
        html = marked.to_html()
        test = "<div><h3>Header</h3><p>Paragraph</p><ul><li>List item one</li><li>List item two</li></ul></div>"
        self.assertEqual(html, test)

        text = """
##### Header

Paragraph **bolded** there

1. List item one
2. List item two
"""
        marked = markdown_to_html_node(text)
        html = marked.to_html()
        test = "<div><h5>Header</h5><p>Paragraph <b>bolded</b> there</p><ol><li>List item one</li><li>List item two</li></ol></div>"
        self.assertEqual(html, test)


if __name__ == "__main__":
    unittest.main()
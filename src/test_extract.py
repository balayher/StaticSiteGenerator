import unittest
from extract import extract_markdown_images, extract_markdown_links, extract_title


class TestExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_markdown_images(text)
        test_tuple = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted, test_tuple)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted = extract_markdown_links(text)
        test_tuple = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extracted, test_tuple)

    def test_extract_title(self):
        text = "# This is a header"
        title = extract_title(text)
        test = "This is a header"
        self.assertEqual(title, test)

        text = """# This is a header
With a lot of other text
that we don't want added
to the file
"""
        title = extract_title(text)
        test = "This is a header"
        self.assertEqual(title, test)
        

if __name__ == "__main__":
    unittest.main()
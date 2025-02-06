import unittest
from blocks import markdown_to_blocks, block_to_block_type


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        
        text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        block = markdown_to_blocks(text)
        test_block = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block\n* This is a list item\n* This is another list item"""
        ]
        self.assertEqual(block, test_block)

        text = "# This is a heading"
        block = markdown_to_blocks(text)
        test_block = [
            "# This is a heading",
        ]
        self.assertEqual(block, test_block)

        text = ""
        block = markdown_to_blocks(text)
        test_block = []
        self.assertEqual(block, test_block)
      
        text = """
# This is a heading

* This is the first list item in a list block
* This is a list item
* This is another list item




Extra long gap
"""
        block = markdown_to_blocks(text)
        #print("Block")
        #print(block)
        test_block = [
            "# This is a heading",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            "Extra long gap"
        ]
        #print("Test")
        #print(test_block)
        self.assertEqual(block, test_block)


    def test_block_block_type(self):
        text = "This is a paragraph"
        block = block_to_block_type(text)
        test_block = "paragraph"
        self.assertEqual(block, test_block)

        text = "### This is a heading"
        block = block_to_block_type(text)
        test_block = "heading"
        self.assertEqual(block, test_block)

        text = "```\nThis is code\n```"
        block = block_to_block_type(text)
        test_block = "code"
        self.assertEqual(block, test_block)

        text = ">This is a quote"
        block = block_to_block_type(text)
        test_block = "quote"
        self.assertEqual(block, test_block)

        text = ">This is a quote\n>but what if\n>MULTIPLE QUOTES?!"
        block = block_to_block_type(text)
        test_block = "quote"
        self.assertEqual(block, test_block)

        text = "* This is a list"
        block = block_to_block_type(text)
        test_block = "unordered_list"
        self.assertEqual(block, test_block)

        text = "- This is a list\n- many of them\n- handle it"
        block = block_to_block_type(text)
        test_block = "unordered_list"
        self.assertEqual(block, test_block)

        text = "1. This list has order"
        block = block_to_block_type(text)
        test_block = "ordered_list"
        self.assertEqual(block, test_block)

        text = "1. This\n2. list\n3. has\n4. order"
        block = block_to_block_type(text)
        test_block = "ordered_list"
        self.assertEqual(block, test_block)

        text = "1. This\n2. list\n3. does\n5. not"
        block = block_to_block_type(text)
        test_block = "paragraph"
        self.assertEqual(block, test_block)

        text = "1. This\n2. list\n* does\n- mixed"
        block = block_to_block_type(text)
        test_block = "paragraph"
        self.assertEqual(block, test_block)


if __name__ == "__main__":
    unittest.main()
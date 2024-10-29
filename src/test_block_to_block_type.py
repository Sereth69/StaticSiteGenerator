import unittest
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), 'heading')

    def test_code(self):
        block = """```
This is a code block
```"""
        self.assertEqual(block_to_block_type(block), 'code')

    def test_quote(self):
        block = """> This is a quote block
> with multiple lines"""
        self.assertEqual(block_to_block_type(block), 'quote')

    def test_unordered_list(self):
        block = """* This is an unordered list
* with multiple items"""
        self.assertEqual(block_to_block_type(block), 'unordered_list')

    def test_ordered_list(self):
        block = """1. This is an ordered list
2. with multiple items"""
        self.assertEqual(block_to_block_type(block), 'ordered_list')

    def test_paragraph(self):
        block = "This is a paragraph of text."
        self.assertEqual(block_to_block_type(block), 'paragraph')

    def test_empty_block(self):
        block = ""
        self.assertEqual(block_to_block_type(block), 'paragraph')

if __name__ == "__main__":
    unittest.main()
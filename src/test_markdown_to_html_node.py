import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected_html = """<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>"""
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.to_html(), expected_html)

    def test_markdown_to_html_node_code_block(self):
        markdown = """```
This is a code block
```"""
        expected_html = """<div><pre><code>This is a code block</code></pre></div>"""
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.to_html(), expected_html)

    def test_markdown_to_html_node_quote_block(self):
        markdown = """> This is a quote block
> with multiple lines"""
        expected_html = """<div><blockquote>This is a quote block\nwith multiple lines</blockquote></div>"""
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.to_html(), expected_html)

    def test_markdown_to_html_node_ordered_list(self):
        markdown = """1. This is an ordered list
2. with multiple items"""
        expected_html = """<div><ol><li>This is an ordered list</li><li>with multiple items</li></ol></div>"""
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.to_html(), expected_html)

    def test_markdown_to_html_node_paragraph(self):
        markdown = "This is a paragraph of text."
        expected_html = """<div><p>This is a paragraph of text.</p></div>"""
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()
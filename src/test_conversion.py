import unittest
from textnode import TextNode, TextType
from conversion import text_node_to_html_node
from leafnode import LeafNode

class TestConversion(unittest.TestCase):
    def test_text_node_to_html_node_normal(self):
        text_node = TextNode("This is normal text", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is normal text")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>This is bold text</b>")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>This is italic text</i>")

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("This is code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>This is code text</code>")

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Click here", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">Click here</a>')

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("Image description", TextType.IMAGE, "https://www.example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com/image.png" alt="Image description" />')

    def test_text_node_to_html_node_invalid_type(self):
        with self.assertRaises(ValueError):
            TextNode("Invalid type", "invalid_type")

if __name__ == "__main__":
    unittest.main()
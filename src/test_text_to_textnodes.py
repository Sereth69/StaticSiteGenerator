import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_text_to_textnodes_no_special(self):
        text = "This is normal text with no special formatting."
        expected_nodes = [TextNode("This is normal text with no special formatting.", TextType.NORMAL)]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_text_to_textnodes_only_bold(self):
        text = "This is **bold** text."
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.NORMAL),
        ]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_text_to_textnodes_only_italic(self):
        text = "This is *italic* text."
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.NORMAL),
        ]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_text_to_textnodes_only_code(self):
        text = "This is `code` text."
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.NORMAL),
        ]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_text_to_textnodes_only_image(self):
        text = "This is an ![image](https://example.com/image.png)."
        expected_nodes = [
            TextNode("This is an ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_text_to_textnodes_only_link(self):
        text = "This is a [link](https://example.com)."
        expected_nodes = [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

if __name__ == "__main__":
    unittest.main()
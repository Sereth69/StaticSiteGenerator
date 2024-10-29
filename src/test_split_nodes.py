import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_image_no_images(self):
        node = TextNode("This is text with no images.", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        expected_nodes = [TextNode("This is text with no images.", TextType.NORMAL)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link_no_links(self):
        node = TextNode("This is text with no links.", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        expected_nodes = [TextNode("This is text with no links.", TextType.NORMAL)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_image_mixed_content(self):
        node = TextNode(
            "This is text with a ![image](https://example.com/image.png) and a link [to example](https://example.com).",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and a link [to example](https://example.com).", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link_mixed_content(self):
        node = TextNode(
            "This is text with a ![image](https://example.com/image.png) and a link [to example](https://example.com).",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a ![image](https://example.com/image.png) and a link ", TextType.NORMAL),
            TextNode("to example", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()
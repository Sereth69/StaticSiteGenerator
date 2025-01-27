import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_no_images(self):
        text = "This is text with no images."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_no_links(self):
        text = "This is text with no links."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_mixed_content(self):
        text = "This is text with a ![image](https://example.com/image.png) and a link [to example](https://example.com)."
        expected_images = [("image", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected_images)

    def test_extract_markdown_links_mixed_content(self):
        text = "This is text with a ![image](https://example.com/image.png) and a link [to example](https://example.com)."
        expected_links = [("to example", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected_links)

if __name__ == "__main__":
    unittest.main()
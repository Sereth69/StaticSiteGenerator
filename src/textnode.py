from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise ValueError("text_type must be an instance of TextType enum")
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        return False

    def __repr__(self):
        return f"TextNode(text='{self.text}', text_type='{self.text_type}', url='{self.url}')"

# Example usage
node1 = TextNode("Hello, world!", TextType.NORMAL)
node2 = TextNode("Hello, world!", TextType.NORMAL)
node3 = TextNode("Click here", TextType.LINK, "http://example.com")

print(node1)  # Output: TextNode(text='Hello, world!', text_type='normal', url='None')
print(node2)  # Output: TextNode(text='Hello, world!', text_type='normal', url='None')
print(node3)  # Output: TextNode(text='Click here', text_type='link', url='http://example.com')

print(node1 == node2)  # Output: True
print(node1 == node3)  # Output: False
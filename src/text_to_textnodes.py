from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

# Example usage
text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
nodes = text_to_textnodes(text)
for node in nodes:
    print(node)
# Output:
# TextNode(text='This is ', text_type='normal', url='None')
# TextNode(text='text', text_type='bold', url='None')
# TextNode(text=' with an ', text_type='normal', url='None')
# TextNode(text='italic', text_type='italic', url='None')
# TextNode(text=' word and a ', text_type='normal', url='None')
# TextNode(text='code block', text_type='code', url='None')
# TextNode(text=' and an ', text_type='normal', url='None')
# TextNode(text='obi wan image', text_type='image', url='https://i.imgur.com/fJRm4Vk.jpeg')
# TextNode(text=' and a ', text_type='normal', url='None')
# TextNode(text='link', text_type='link', url='https://boot.dev')
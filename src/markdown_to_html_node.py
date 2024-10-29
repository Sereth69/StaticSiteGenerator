from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from text_to_textnodes import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL.value:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD.value:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC.value:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE.value:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK.value:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE.value:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Unknown TextType")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == 'heading':
            level = len(block.split(' ')[0])
            content = block[level + 1:]
            block_node = ParentNode(f"h{level}", text_to_children(content))
        elif block_type == 'code':
            content = block[3:-3].strip()
            block_node = ParentNode("pre", [LeafNode("code", content)])
        elif block_type == 'quote':
            content = '\n'.join(line[1:].strip() for line in block.split('\n'))
            block_node = ParentNode("blockquote", text_to_children(content))
        elif block_type == 'unordered_list':
            items = block.split('\n')
            children = [ParentNode("li", text_to_children(item[2:])) for item in items]
            block_node = ParentNode("ul", children)
        elif block_type == 'ordered_list':
            items = block.split('\n')
            children = [ParentNode("li", text_to_children(item.split('. ', 1)[1])) for item in items]
            block_node = ParentNode("ol", children)
        else:  # paragraph
            block_node = ParentNode("p", text_to_children(block))

        block_nodes.append(block_node)

    return ParentNode("div", block_nodes)

# Example usage
markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

html_node = markdown_to_html_node(markdown)
print(html_node.to_html())
# Output:
# <div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>
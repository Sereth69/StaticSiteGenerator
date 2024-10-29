from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL.value:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Unmatched delimiter found in text")

        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part:
                    new_nodes.append(TextNode(part, TextType.NORMAL))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

# Example usage
node = TextNode("This is text with a `code block` word", TextType.NORMAL)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
for n in new_nodes:
    print(n)
# Output:
# TextNode(text='This is text with a ', text_type='normal', url='None')
# TextNode(text='code block', text_type='code', url='None')
# TextNode(text=' word', text_type='normal', url='None')
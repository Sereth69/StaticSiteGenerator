from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL.value:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(node)
            continue

        for alt_text, url in images:
            parts = text.split(f"![{alt_text}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            text = parts[1]

        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL.value:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue

        for anchor_text, url in links:
            parts = text.split(f"[{anchor_text}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            text = parts[1]

        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL))

    return new_nodes

# Example usage
node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.NORMAL,
)
new_nodes = split_nodes_link([node])
for n in new_nodes:
    print(n)
# Output:
# TextNode(text='This is text with a link ', text_type='normal', url='None')
# TextNode(text='to boot dev', text_type='link', url='https://www.boot.dev')
# TextNode(text=' and ', text_type='normal', url='None')
# TextNode(text='to youtube', text_type='link', url='https://www.youtube.com/@bootdotdev')
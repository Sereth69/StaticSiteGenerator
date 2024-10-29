def markdown_to_blocks(markdown):
    # Split the markdown string into blocks based on blank lines
    blocks = markdown.split('\n\n')
    
    # Strip leading and trailing whitespace from each block and each line within the block
    blocks = ['\n'.join(line.strip() for line in block.split('\n')).strip() for block in blocks]
    
    # Remove any empty blocks
    blocks = [block for block in blocks if block]
    
    return blocks

# Example usage
markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

blocks = markdown_to_blocks(markdown)
for block in blocks:
    print(f"Block:\n{block}\n")
# Output:
# Block:
# # This is a heading
#
# Block:
# This is a paragraph of text. It has some **bold** and *italic* words inside of it.
#
# Block:
# * This is the first list item in a list block
# * This is a list item
# * This is another list item
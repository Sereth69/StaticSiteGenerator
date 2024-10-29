def block_to_block_type(block):
    lines = block.split('\n')
    
    # Check for heading
    if lines[0].startswith('#'):
        if 1 <= len(lines[0].split(' ')[0]) <= 6:
            return 'heading'
    
    # Check for code block
    if block.startswith('```') and block.endswith('```'):
        return 'code'
    
    # Check for quote block
    if all(line.startswith('>') for line in lines):
        return 'quote'
    
    # Check for unordered list block
    if all(line.startswith('* ') or line.startswith('- ') for line in lines):
        return 'unordered_list'
    
    # Check for ordered list block
    if all(line.split('. ')[0].isdigit() and int(line.split('. ')[0]) == i + 1 for i, line in enumerate(lines)):
        return 'ordered_list'
    
    # Default to paragraph
    return 'paragraph'

# Example usage
block = """# This is a heading"""
print(block_to_block_type(block))  # Output: heading

block = """```
This is a code block
```"""
print(block_to_block_type(block))  # Output: code

block = """> This is a quote block
> with multiple lines"""
print(block_to_block_type(block))  # Output: quote

block = """* This is an unordered list
* with multiple items"""
print(block_to_block_type(block))  # Output: unordered_list

block = """1. This is an ordered list
2. with multiple items"""
print(block_to_block_type(block))  # Output: ordered_list

block = """This is a paragraph of text."""
print(block_to_block_type(block))  # Output: paragraph
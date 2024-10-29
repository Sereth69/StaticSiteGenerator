class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")

    def props_to_html(self):
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"

# Example usage
node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
print(node)  # Output: HTMLNode(tag='a', value='Click here', children=[], props={'href': 'https://www.google.com', 'target': '_blank'})
print(node.props_to_html())  # Output:  href="https://www.google.com" target="_blank"
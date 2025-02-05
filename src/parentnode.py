from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag not found")
        
        if not self.children:
            raise ValueError("Children not found, check your milk box")

        children_value = ""
        for child in self.children:
            children_value += child.to_html()
            
        props_string = self.props_to_html()
        return f'<{self.tag}{props_string}>{children_value}</{self.tag}>'
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
class HtmlNode:
    """
    An HTMLNode without:
    ============================================
    a tag      -->   renders as raw text
    a value    -->   is assumed to have children
    children   -->   is assumed to have a value
    props      -->   won't have any attributes
    ============================================
    """

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return " "
        
        props_html = " ".join(map(lambda item: f'{item[0]}="{item[1]}"', self.props.items()))

        return f" {props_html}"
    
    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"

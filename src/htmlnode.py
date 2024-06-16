class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented yet")
    
    def props_to_html(self):
        propshtml = ""
        if self.props == None:
            return propshtml
        for prop in self.props:
            propshtml += f" {prop}={self.props[prop]}"
        return propshtml
    
    def __repr__(self):
        return f"HTMLnode({self.tag}, {self.value}, {self.children}, {self.props})"
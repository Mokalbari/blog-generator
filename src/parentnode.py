from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is mandatory")

        if self.children is None:
            raise ValueError("children is mandatory")

        open_close_tag = (f"<{self.tag}>", f"</{self.tag}>")

        child_html = []
        for child in self.children:
            child_html.append(child.to_html())

        return open_close_tag[0] + "".join(child_html) + open_close_tag[1]

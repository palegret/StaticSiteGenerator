from models.leafnode import LeafNode
from models.texttype import TextType


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode(None, self.text)
        elif self.text_type == TextType.BOLD:
            return LeafNode("b", self.text)
        elif self.text_type == TextType.ITALIC:
            return LeafNode("i", self.text)
        elif self.text_type == TextType.CODE:
            return LeafNode("code", self.text)
        elif self.text_type == TextType.LINK:
            return LeafNode("a", self.text, {"href": self.url})
        elif self.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": self.url, "alt": self.text})
        else:
            raise ValueError(f"invalid text type: {self.text_type}")

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode(text=\"{self.text}\", text_type={self.text_type}, url=\"{self.url if self.url else ""}\")"

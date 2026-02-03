import unittest

from src.text_node_to_html_node import text_node_to_html_node
from src.textnode import TextNode, TextType

FAKE_LINK = "https://link.com"


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "text")

    def test_link(self):
        node = TextNode("link", TextType.LINK, url=FAKE_LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": FAKE_LINK})

    def test_image(self):
        node = TextNode("image", TextType.IMAGE, url=FAKE_LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": FAKE_LINK, "alt": "image"})

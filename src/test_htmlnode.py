import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        p_node = HTMLNode(tag="p", value="Hello node")
        p_node_2 = HTMLNode(tag="p", value="Hello node")

        self.assertEqual(p_node, p_node_2)

        a_node = HTMLNode(
            tag="a",
            value="this is a link",
            props={"href": "https://bootdev.com", "target": "_blank"},
        )
        expected_props = "href=https://bootdev.com target=_blank"
        self.assertEqual(a_node.props_to_html(), expected_props)
        self.assertNotEqual(a_node, p_node)

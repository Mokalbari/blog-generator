import unittest

from src.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leaf_node = LeafNode(tag="p", value="i'm a leaf")
        another_leaf = LeafNode(tag="p", value="i'm a leaf")

        should_print_leaf = "<p>i'm a leaf</p>"
        self.assertEqual(leaf_node, another_leaf)
        self.assertEqual(leaf_node.to_html(), should_print_leaf)

        leaf_with_props = LeafNode(
            tag="a",
            value="i'm a link",
            props={"href": "https://bootdev.com", "target": "_blank"},
        )
        should_print_link = (
            "<a href='https://bootdev.com' target='_blank'>i'm a link</a>"
        )
        self.assertEqual(leaf_with_props.to_html(), should_print_link)

    def test_error(self):
        error_node = LeafNode("p", value=None)
        with self.assertRaises(ValueError):
            error_node.to_html()

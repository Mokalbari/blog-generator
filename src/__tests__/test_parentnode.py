import unittest

from src.leafnode import LeafNode
from src.parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_in_parent(self):
        child_a = LeafNode("p", "child_a")
        child_b = LeafNode("p", "child_b")

        parent = ParentNode("div", [child_a, child_b])
        another_parent = ParentNode("div", [parent])

        self.assertEqual(
            another_parent.to_html(),
            "<div><div><p>child_a</p><p>child_b</p></div></div>",
        )

import unittest

from src.split_node_delimiter import split_node_delimiter
from src.textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_basic_case(self):
        old_node = TextNode("text", TextType.BOLD)
        new_node = split_node_delimiter(old_node, "`", TextType.CODE)
        self.assertEqual(new_node, [old_node])

    def test_simple_markdown(self):
        old_node = TextNode("text `code` and some text", TextType.TEXT)
        new_node = split_node_delimiter(old_node, "`", TextType.CODE)
        self.assertEqual(
            new_node,
            [
                TextNode("text ", TextType.TEXT, None),
                TextNode("code", TextType.CODE, None),
                TextNode(" and some text", TextType.TEXT, None),
            ],
        )

    def test_bold(self):
        old_node = TextNode("text **bold** and some text", TextType.TEXT)
        new_node = split_node_delimiter(old_node, "**", TextType.BOLD)
        self.assertEqual(
            new_node,
            [
                TextNode("text ", TextType.TEXT, None),
                TextNode("bold", TextType.BOLD, None),
                TextNode(" and some text", TextType.TEXT, None),
            ],
        )

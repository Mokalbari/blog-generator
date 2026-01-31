import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("This is an italic node", TextType.ITALIC)
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is another type of node", TextType.CODE)
        self.assertNotEqual(node, node4)


if __name__ == "__main__":
    unittest.main()

import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
        self.assertEqual(node, node2)

    def test_neq_on_text(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
        node2 = TextNode("This is ANOTHER text node", TextType.BOLD, "https://www.boot.dev/")
        self.assertNotEqual(node, node2)

    def test_neq_on_texttype(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
        node2 = TextNode("This is a text node", TextType.NORMAL, "https://www.boot.dev/")
        self.assertNotEqual(node, node2)

    def test_neq_on_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.blizzard.com/")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

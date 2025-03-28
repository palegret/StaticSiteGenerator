import unittest
from models.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        expected = "<p>Hello, world!</p>"

        actual = LeafNode(
            tag="p", 
            value="Hello, world!",
            props=None
        ).to_html()

        self.assertEqual(expected, actual)

    def test_leaf_to_html_a(self):
        expected = '<a href="https://www.google.com">Click me!</a>'

        actual = LeafNode(
            tag="a", 
            value="Click me!", 
            props={ "href": "https://www.google.com" }
        ).to_html()

        self.assertEqual(expected, actual)

    def test_leaf_to_html_no_tag(self):
        expected = "Hello, world!"

        actual = LeafNode(
            tag=None, 
            value="Hello, world!",
            props=None 
        ).to_html()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
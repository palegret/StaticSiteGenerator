import unittest

from models.htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_html_has_value_with_props(self):
        node = HtmlNode(props={"id": "test", "class": "test"})
        node_props_html = node.props_to_html()
        expected = ' id="test" class="test"'
        self.assertEqual(node_props_html, expected)

    def test_html_has_no_props(self):
        node = HtmlNode()
        node_props_html = node.props_to_html()
        expected = ''
        self.assertEqual(node_props_html, expected)

    def test_html_has_value_with_one_prop(self):
        node = HtmlNode(props={"id": "test"})
        node_props_html = node.props_to_html()
        expected = ' id="test"'
        self.assertEqual(node_props_html, expected)

    # vvv TESTS BELOW HERE ARE FROM THE SOLUTION vvv

    def test_to_html_props(self):
        node = HtmlNode(tag="div", value="Hello, world!", children=None, props={"class": "greeting", "href": "https://boot.dev"})
        expected_props_html = ' class="greeting" href="https://boot.dev"'
        self.assertEqual(node.props_to_html(), expected_props_html)

    def test_values(self):
        node = HtmlNode(tag="div", value="I wish I could read", children=None, props=None)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HtmlNode(tag="p", value="What a strange world", children=None, props={"class": "primary"})
        expected_repr = "HtmlNode(p, What a strange world, None, {'class': 'primary'})"
        self.assertEqual(node.__repr__(), expected_repr)


if __name__ == "__main__":
    unittest.main()

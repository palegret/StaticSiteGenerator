import unittest

from models.textnode import TextNode, TextType

from shared.inline_markdown_utils import (
    text_to_textnodes,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_links,
    extract_markdown_images,
)


class TestInlineMarkdownUtils(unittest.TestCase):
    def test_delim_bold(self):
        old_nodes = [TextNode("This is text with a **bolded** word", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(expected, new_nodes)

    def test_delim_bold_double(self):
        old_nodes = [TextNode("This is text with a **bolded** word and **another**", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" word and ", TextType.TEXT),
            TextNode("another", TextType.BOLD),
        ]

        self.assertListEqual(expected, new_nodes)

    def test_delim_bold_multiword(self):
        old_nodes = [TextNode("This is text with a **bolded word** and **another**", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded word", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("another", TextType.BOLD)
        ]

        self.assertListEqual(expected, new_nodes)

    def test_delim_italic(self):
        old_nodes = [TextNode("This is text with an _italic_ word", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)

        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(expected, new_nodes)

    def test_delim_bold_and_italic(self):
        old_nodes = [TextNode("**bold** and _italic_", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)

        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]
        
        self.assertListEqual(expected, new_nodes)

    def test_delim_code(self):
        old_nodes = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertListEqual(expected, new_nodes)

    def test_extract_markdown_images(self):
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")

        self.assertListEqual(expected, matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)")
        expected = [
            ("link", "https://boot.dev"),
            ("another link", "https://blog.boot.dev"),
        ]

        self.assertListEqual(expected, matches)

    def test_split_image(self):
        old_nodes = [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)]
        new_nodes = split_nodes_image(old_nodes)

        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ]

        self.assertListEqual(expected, new_nodes)

    def test_split_image_single(self):
        old_nodes = [TextNode("![image](https://www.example.COM/IMAGE.PNG)", TextType.TEXT)]
        new_nodes = split_nodes_image(old_nodes)
        expected = [TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG")]

        self.assertListEqual(expected, new_nodes)

    def test_split_images(self):
        old_nodes = [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)]
        new_nodes = split_nodes_image(old_nodes)

        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
        ]
        
        self.assertListEqual(expected, new_nodes)

    def test_split_links(self):
        old_nodes = [TextNode("This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows", TextType.TEXT)]
        new_nodes = split_nodes_link(old_nodes)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
            TextNode(" with text that follows", TextType.TEXT)
        ]

        self.assertListEqual(expected, new_nodes)

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)")

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertListEqual(expected, nodes)


if __name__ == "__main__":
    unittest.main()

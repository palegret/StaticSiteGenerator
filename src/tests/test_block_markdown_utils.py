import unittest

from models.blocktype import BlockType

from shared.block_markdown_utils import (
    markdown_to_blocks,
    markdown_to_html_node,
    block_to_block_type,
)


class TestBlockMarkdownUtils(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(markdown)

        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]

        self.assertEqual(expected, blocks)

    def test_block_to_block_type(self):
        block = "This is a paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

        block = "- This is a list item\n- with another item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

        block = "1. This is an ordered list item\n2. with another item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

        block = "### This is a header"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

        block = "```This is a code block```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

        block = "> This is a quote\n> This is another line of the quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_paragraph(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

"""

        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(expected, html)

    def test_paragraphs(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(expected, html)

    def test_lists(self):
        markdown = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        expected = "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(expected, html)

    def test_headings(self):
        markdown = """
# this is an h1

this is paragraph text

## this is an h2
"""

        expected = "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(expected, html)

    def test_blockquote(self):
        markdown = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(markdown)
        html = node.to_html()
        expected = "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>"
        self.assertEqual(expected, html)

    def test_code(self):
        markdown = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(markdown)
        html = node.to_html()
        expected = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        self.assertEqual(expected, html)


if __name__ == "__main__":
    unittest.main()

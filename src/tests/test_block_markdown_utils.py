import unittest

from models.blocktype import BlockType

from shared.block_markdown_utils import (
    markdown_to_blocks,
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


if __name__ == "__main__":
    unittest.main()

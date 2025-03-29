import re

from models.blocktype import BlockType


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    filtered_blocks = []

    for block in blocks:
        if block == "":
            continue

        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks


def block_to_block_type(markdown):
    is_code_block = lambda line: line.startswith("```") and line.endswith("```")
    is_quote_block = lambda line: all(line.startswith(">") for line in markdown.splitlines())
    is_unordered_list = lambda line: all(line.startswith("- ") for line in markdown.splitlines())
    is_ordered_list = lambda line: all(re.match(r"^\d+\.\s", line) for line in markdown.splitlines())
    is_heading = lambda line: re.match(r"^#{1,6} ", line) is not None
    get_heading_level = lambda line: len(line.split()[0]) if is_heading(line) else 0
    
    if is_heading(markdown):
        heading_level = get_heading_level(markdown)

        if heading_level < 1 or heading_level > 6:
            raise ValueError("Invalid heading level")

        return BlockType.HEADING
    
    if is_code_block(markdown):
        return BlockType.CODE
    
    if is_quote_block(markdown):
        return BlockType.QUOTE
    
    if is_unordered_list(markdown):
        return BlockType.UNORDERED_LIST
    
    if is_ordered_list(markdown):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

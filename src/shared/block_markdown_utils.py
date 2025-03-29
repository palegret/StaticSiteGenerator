import re

from models.blocktype import BlockType
from models.parentnode import ParentNode
from models.textnode import TextNode
from models.texttype import TextType
from shared.inline_markdown_utils import text_to_textnodes


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    filtered_blocks = []

    for block in blocks:
        if block == "":
            continue

        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks


def is_code_block(markdown):
    return markdown.startswith("```") and markdown.endswith("```")


def is_quote_block(markdown):
    return all(line.startswith(">") for line in markdown.splitlines())


def block_to_block_type(markdown):
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


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node.to_html_node()
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not is_code_block(block):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = raw_text_node.to_html_node()
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def ordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def unordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    if not is_quote_block(block):
        raise ValueError("invalid quote block")
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

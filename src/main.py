from pprint import pprint

from models.textnode import TextNode
from models.texttype import TextType


def main():
    pprint(TextNode(
        text="This is some anchor text", 
        text_type=TextType.LINK, 
        url="https://www.boot.dev/"
    ))
    

main()

from models.textnode import TextNode
from models.texttype import TextType


def main():
    print(TextNode(
        text="This is some anchor text", 
        text_type=TextType.LINK, 
        url="https://www.boot.dev/"
    ))
    

main()

import sys

from generate import generate_pages_recursive
from publish import publish_static_content


def main():
    print("Welcome to the Static Site Generator!")

    basepath = "/"

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Publishing static files...")

    publish_static_content(
        source_directory="./static", 
        destination_directory = "./docs"
    )

    print(f"Generating site content, basepath is set to '{basepath}'...")

    generate_pages_recursive(
        source_path="./content",
        template_path="./template.html",
        destination_path="./docs",
        basepath=basepath
    )
    

main()

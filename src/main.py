from generate import generate_pages_recursive
from publish import publish_static_content


def main():
    print("Starting the Static Site Generator...")

    print("Publishing static files...")

    publish_static_content(
        source_directory="./static", 
        destination_directory = "./public"
    )

    print("Generating site content...")

    generate_pages_recursive(
        source_path="./content",
        template_path="./template.html",
        destination_path="./public",
    )
    

main()

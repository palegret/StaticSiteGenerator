import os

from generate import generate_page
from publish import publish_static_content


def main():
    print("Starting the Static Site Generator...")

    publish_static_content(
        source_directory="static", 
        destination_directory = "public"
    )

    generate_page(
        from_path=os.path.join("./content/blog/glorfindel", "index.md"),
        template_path="./template.html",
        dest_path=os.path.join("./public/blog/glorfindel", "index.html"),
    )

    generate_page(
        from_path=os.path.join("./content/blog/majesty", "index.md"),
        template_path="./template.html",
        dest_path=os.path.join("./public/blog/majesty", "index.html"),
    )

    generate_page(
        from_path=os.path.join("./content/blog/tom", "index.md"),
        template_path="./template.html",
        dest_path=os.path.join("./public/blog/tom", "index.html"),
    )

    generate_page(
        from_path=os.path.join("./content/contact", "index.md"),
        template_path="./template.html",
        dest_path=os.path.join("./public/contact", "index.html"),
    )

    generate_page(
        from_path=os.path.join("./content", "index.md"),
        template_path="./template.html",
        dest_path=os.path.join("./public", "index.html"),
    )
    

main()

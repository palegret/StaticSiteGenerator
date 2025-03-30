from publish import publish_static_content


def main():
    print("Starting the Static Site Generator...")
    publish_static_content(source_directory="static", destination_directory = "public")
    

main()

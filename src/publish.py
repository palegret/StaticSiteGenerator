import os
import shutil

def publish_static_content(source_directory, destination_directory):
    print("Publishing static files...")

    if not os.path.exists(source_directory):
        print(f"Source directory '{source_directory}' does not exist.")
        return

    if os.path.exists(destination_directory):
        shutil.rmtree(destination_directory)
        print(f"Removed existing destination directory '{destination_directory}'.")

    os.makedirs(destination_directory)
    print(f"Created destination directory '{destination_directory}'.")

    for root, dirs, files in os.walk(source_directory):
        dest_dir = os.path.join(destination_directory, os.path.relpath(root, source_directory))
        os.makedirs(dest_dir, exist_ok=True)
        print(f"Created directory '{dest_dir}'.")

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy(src_file, dest_file)
            print(f"Copied '{src_file}' to '{dest_file}'.")

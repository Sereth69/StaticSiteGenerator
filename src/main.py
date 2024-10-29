import os
import shutil
from textnode import TextNode, TextType
from copy_static import copy_directory
from generate_page import generate_page  # Import the generate_page function

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + '.html')
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                generate_page(from_path, template_path, dest_path)

def main():
    # Delete anything in the public directory
    if os.path.exists('public'):
        shutil.rmtree('public')

    # Copy static files to public directory
    copy_directory("static", "public")

    # Generate pages recursively from content directory using template.html
    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == "__main__":
    main()
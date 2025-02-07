import os
import shutil

from md_to_html import markdown_to_html_node
from htmlnode import HTMLNode
from extract import extract_title

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_from_static(dir_path_static, dir_path_public)
    generate_page("./content/index.md", "./template.html", "./public/index.html")

def copy_from_static(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    
    for item in os.listdir(source):
        from_path = os.path.join(source, item)
        to_path = os.path.join(destination, item)
        print(f" * {from_path} -> {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_from_static(from_path, to_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.buffer

    node = markdown_to_html_node(markdown)
    md_string = node.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", md_string)
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()

    

main()
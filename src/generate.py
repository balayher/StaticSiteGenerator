import os
import shutil
from pathlib import Path

from md_to_html import markdown_to_html_node
from extract import extract_title

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
    from_file.close()
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown)
    md_string = node.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", md_string)
    dest_dir = os.path.dirname(dest_path)
    if os.path.exists(dest_dir) != "":
        os.makedirs(dest_dir, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path, exist_ok=True)
    
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        to_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(from_path):
            to_path = Path(to_path).with_suffix(".html")
            generate_page(from_path, template_path, to_path)
        else:
            generate_pages_recursive(from_path, template_path, to_path)
    return
import os
import frontmatter

metadata_template = """---
title: {}
date: {}
---

{}"""

def has_metadata(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    try:
        frontmatter.load(content)
        return True
    except Exception:
        return False

def generate_metadata(file_path):
    if has_metadata(file_path):
        print(f"Skipping {file_path} (metadata already exists)")
        return

    file_name = os.path.basename(file_path)
    date, title = file_name.split("-", 2)[0:2]
    if len(file_name.split("-")) < 3:
        print(f"Skipping {file_path} (file_name not fixed)")
        return

    with open(file_path, "r") as file:
        content = file.read()

    metadata_content = metadata_template.format(title, date, content)

    with open(file_path, "w") as file:
        file.write(metadata_content)
        print(f"Generated metadata for {file_path}")

# Iterate through all Markdown files in the repository and generate metadata
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            generate_metadata(file_path)

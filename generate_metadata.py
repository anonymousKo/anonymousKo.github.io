import os
import frontmatter
import subprocess

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
    if len(file_name) >= 12 and file_name[4] == "-" and file_name[7] == "-":
        date, title = file_name.split("-", 2)[0:2]
    else:
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
            
# Stage the files you want to commit
subprocess.run(["git", "add", "content/posts"])

# Commit the changes
subprocess.run(["git", "commit", "-m", "Add metadata"])

# Push the changes
subprocess.run(["git", "push"])

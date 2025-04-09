import os
import re

# Set this to your Obsidian vault root
vault_path = r"C:\Users\brand\Obsidian\CyberSec-Notes"

# Regex to find image links like ![[Pasted image 20250409xxxx.png]]
pasted_pattern = re.compile(r'!\[\[(Pasted image.*?\.png)\]\]')

# Track changed files
updated_files = []

# Walk through all .md files in the vault
for root, dirs, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            matches = pasted_pattern.findall(content)
            if not matches:
                continue

            updated_content = content
            changed = False

            for match in matches:
                base_name = os.path.splitext(match)[0]
                images_folder = os.path.join(root, "images")

                if not os.path.isdir(images_folder):
                    continue

                # Find any renamed image that starts with the base name
                for img_file in os.listdir(images_folder):
                    if img_file.startswith(base_name) and img_file.endswith((".png", ".jpg", ".jpeg")):
                        updated_link = f"![[images/{img_file}]]"
                        original_link = f"![[{match}]]"
                        updated_content = updated_content.replace(original_link, updated_link)
                        changed = True
                        break

            if changed:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                updated_files.append(file_path)

# Summary output
print("✅ Updated the following files:")
for f in updated_files:
    print(" -", f)

if not updated_files:
    print("ℹ️ No image links needed updating.")

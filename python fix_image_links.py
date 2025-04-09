import os
import re

vault_path = r"C:\Users\brand\Obsidian\CyberSec-Notes"
image_extensions = ('.png', '.jpg', '.jpeg')
image_link_pattern = re.compile(r'!\[\[(.+?\.(?:png|jpg|jpeg))\]\]', re.IGNORECASE)

updated_files = []

for root, dirs, files in os.walk(vault_path):
    for file in files:
        if not file.endswith(".md"):
            continue

        file_path = os.path.join(root, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        matches = image_link_pattern.findall(content)
        if not matches:
            continue

        changed = False
        updated_content = content
        images_dir = os.path.join(root, "images")

        if not os.path.isdir(images_dir):
            continue

        available_images = set(os.listdir(images_dir))

        for match in matches:
            current_filename = os.path.basename(match)
            current_ext = os.path.splitext(current_filename)[1].lower()

            if current_filename in available_images:
                new_link = f"![[images/{current_filename}]]"
                old_link = f"![[{match}]]"
                if old_link != new_link:
                    updated_content = updated_content.replace(old_link, new_link)
                    changed = True

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            updated_files.append(file_path)

# Output result
if updated_files:
    print("✅ Fixed image link paths in:")
    for f in updated_files:
        print(" -", f)
else:
    print("ℹ️ All image links already point to images/ subfolders correctly.")

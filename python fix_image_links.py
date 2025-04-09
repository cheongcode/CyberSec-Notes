import os
import re
import shutil

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
            os.makedirs(images_dir)

        for match in matches:
            src_filename = os.path.basename(match)
            src_path = os.path.join(root, src_filename)
            dest_path = os.path.join(images_dir, src_filename)

            if not os.path.isfile(dest_path):
                if os.path.isfile(src_path):
                    shutil.move(src_path, dest_path)
                    print(f"📂 Moved {src_filename} → images/")
                    changed = True
                else:
                    continue  # File doesn't exist anywhere

            # Fix the link if needed
            if not match.startswith("images/"):
                old_link = f"![[{match}]]"
                new_link = f"![[images/{src_filename}]]"
                updated_content = updated_content.replace(old_link, new_link)
                changed = True

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            updated_files.append(file_path)

# Summary output
if updated_files:
    print("✅ Updated notes:")
    for f in updated_files:
        print(" -", f)
else:
    print("ℹ️ All images already inside /images/ and links are correct.")

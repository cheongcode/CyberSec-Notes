import os
import re
import shutil
from PIL import Image

vault_path = r"C:\Users\brand\Obsidian\CyberSec-Notes"
image_link_pattern = re.compile(r'!\[\[(.+?\.(?:png|jpg|jpeg))\]\]', re.IGNORECASE)

def convert_to_jpg(src_path, dst_path):
    img = Image.open(src_path).convert("RGB")
    img.save(dst_path, "JPEG", quality=85)
    img.close()
    os.remove(src_path)

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
            original_link = f"![[{match}]]"
            src_filename = os.path.basename(match)
            src_path = os.path.join(root, src_filename)

            # If the file is not in the current folder, maybe it's already inside images/
            if not os.path.isfile(src_path):
                src_path = os.path.join(images_dir, src_filename)
                if not os.path.isfile(src_path):
                    continue  # File doesn't exist at all, skip

            base_name, ext = os.path.splitext(src_filename)
            ext = ext.lower()

            target_name = base_name + ".jpg"
            target_path = os.path.join(images_dir, target_name)
            new_link = f"![[images/{target_name}]]"

            if ext == ".png":
                convert_to_jpg(src_path, target_path)
                changed = True
            elif ext == ".jpeg":
                shutil.move(src_path, target_path)
                changed = True
            elif ext == ".jpg" and os.path.dirname(src_path) != images_dir:
                shutil.move(src_path, target_path)
                changed = True

            if original_link != new_link:
                updated_content = updated_content.replace(original_link, new_link)

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            updated_files.append(file_path)

# Summary output
if updated_files:
    print("✅ Updated the following notes:")
    for f in updated_files:
        print(" -", f)
else:
    print("ℹ️ All notes and image paths are already correct.")

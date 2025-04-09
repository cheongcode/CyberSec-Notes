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
            filename = os.path.basename(match)
            old_link = f"![[{match}]]"
            new_link = f"![[images/{filename}]]"

            src_path = os.path.join(root, filename)
            dst_path = os.path.join(images_dir, filename)

            if os.path.isfile(src_path) and not os.path.isfile(dst_path):
                shutil.move(src_path, dst_path)
                print(f"📦 Moved: {filename} → {images_dir}")
                changed = True

            if old_link != new_link:
                updated_content = updated_content.replace(old_link, new_link)
                changed = True

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            updated_files.append(file_path)

# Result
if updated_files:
    print("✅ Updated the following notes:")
    for f in updated_files:
        print(" -", f)
else:
    print("ℹ️ No changes were needed.")

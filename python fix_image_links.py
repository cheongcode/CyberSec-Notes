import os
import re
from PIL import Image

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

        for match in matches:
            current_filename = os.path.basename(match)
            old_ext = os.path.splitext(current_filename)[1].lower()
            base_name = os.path.splitext(current_filename)[0]

            original_image_path = os.path.join(images_dir, current_filename)

            if not os.path.isfile(original_image_path):
                continue

            # If it's a PNG, convert it
            if old_ext == ".png":
                jpg_filename = base_name + ".jpg"
                jpg_path = os.path.join(images_dir, jpg_filename)

                try:
                    img = Image.open(original_image_path).convert("RGB")
                    img.save(jpg_path, "JPEG", quality=85)
                    img.close()
                    os.remove(original_image_path)
                    print(f"✔ Converted: {current_filename} → {jpg_filename}")
                except Exception as e:
                    print(f"✘ Failed to convert {current_filename}: {e}")
                    continue

                old_link = f"![[{match}]]"
                new_link = f"![[images/{jpg_filename}]]"
                updated_content = updated_content.replace(old_link, new_link)
                changed = True

            # If it's already jpg/jpeg but not inside images/
            elif not match.startswith("images/"):
                new_link = f"![[images/{current_filename}]]"
                old_link = f"![[{match}]]"
                updated_content = updated_content.replace(old_link, new_link)
                changed = True

        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            updated_files.append(file_path)

# Output summary
if updated_files:
    print("✅ Processed and updated:")
    for f in updated_files:
        print(" -", f)
else:
    print("ℹ️ No changes were necessary.")

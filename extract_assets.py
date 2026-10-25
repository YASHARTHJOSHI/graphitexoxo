import zipfile
import os
import shutil

zip_path = r"C:\Users\Demo\Downloads\GRAPHITE26_ANTIGRAVITY_ASSET_PACK.zip"
target_dir = r"c:\Users\Demo\Downloads\qwqw\assets"
os.makedirs(target_dir, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as z:
    for member in z.infolist():
        if member.filename.startswith("GRAPHITE26_ANTIGRAVITY_ASSETS/images/") and not member.is_dir():
            filename = os.path.basename(member.filename)
            dest = os.path.join(target_dir, filename)
            with z.open(member) as source, open(dest, "wb") as target:
                shutil.copyfileobj(source, target)
            print(f"Extracted image: {filename}")
        elif member.filename.endswith("README.txt"):
            filename = os.path.basename(member.filename)
            dest = os.path.join(target_dir, filename)
            with z.open(member) as source, open(dest, "wb") as target:
                shutil.copyfileobj(source, target)
            print(f"Extracted: {filename}")

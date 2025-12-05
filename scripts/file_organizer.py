import os
import shutil
from datetime import datetime

def run(folder):
    if not os.path.exists(folder):
        print(f"❌ Folder not found: {folder}")
        return

    print(f"\n📂 Organizing files in: {folder}\n")

    categories = {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".pdf", ".txt", ".docx", ".xlsx"],
        "Archives": [".zip", ".tar", ".gz", ".rar"],
        "Scripts": [".py", ".sh", ".js"],
        "Others": []
    }

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        moved = False

        for category, extensions in categories.items():
            if ext.lower() in extensions:
                dest_folder = os.path.join(folder, category)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                break

        if not moved:
            dest_folder = os.path.join(folder, "Others")
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, filename))

    with open("logs/file_organizer.log", "a") as log:
        log.write(f"{datetime.now()} - Organized files in {folder}\n")

    print("✔ File organization completed!\n")

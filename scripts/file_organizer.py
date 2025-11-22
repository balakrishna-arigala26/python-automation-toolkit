import os
import shutil
from datetime import datetime

SOURCE_FOLDER = "/home/balu/Downloads"  # change to your folder path
DESTINATION_FOLDER = "../organized-files"

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".tar", ".gz"],
    "Scripts": [".py", ".sh", ".pl"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3", ".wav"],

 } 

def organize_files():
    logs = []
    try:
        files = os.listdir(SOURCE_FOLDER)

        for file in files:
            file_path = os.path.join(SOURCE_FOLDER, file)

            if os.path.isfile(file_path):
                _, ext = os.path.splitext(file)


                # check which folder the file belongs to
                moved = False
                for folder, extensions in FILE_TYPES.items():
                    if ext.lower() in extensions:
                        dest_folder = os.path.join(DESTINATION_FOLDER, folder)
                        os.makedirs(dest_folder, exist_ok=True)

                        shutil.move(file_path, dest_folder)
                        logs.append(f"{datetime.now()} - Moved {file} to {folder}")
                        moved = True
                        break
                
                # If no matching extension
                if not moved:
                    other_folder = os.path.join(DESTINATION_FOLDER, "Others")
                    os.makedirs(other_folder, exist_ok=True)

                    shutil.move(file_path, other_folder)
                    logs.append(f"{datetime.now()} - Moved {file}  to Others")


        return logs

    except Exception as e:
        return [f"{datetime.now()} - Error: {str(e)}"]


if __name__ == "__main__":
    log_entries = organize_files()

    # Write logs
    with open("../logs/file_organizer.log", "a") as log_file:
        for entry in log_entries:
            log_file.write(entry + "\n")

    print("File organization completed. Check logs/file_organizer.log")

import os
from datetime import datetime

def run(path):
    print(f"\nListing files in: {path}\n")
    files = os.listdir(path)
    for f in files:
        print(f"- {f}")

    with open("logs/list_files.log", "a") as log:
        log.write(f"{datetime.now()} - Listed files in {path}\n")

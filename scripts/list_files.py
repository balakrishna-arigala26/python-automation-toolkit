import os
from datetime import datetime

def list_files(path):
    try:
        print(f"\nListing files in: {path}\n")

        files = os.listdir(path)
        for f in files:
            print(f"- {f}")

        log_message = f"{datetime.now()} - Listed files in {path}\n"
        return log_message

    except Exception as e:
        error_message = f"{datetime.now()} - Error listing files: {str(e)}\n"
        return error_message

if __name__ == "__main__":
    folder = "/home"        # change this to any folder you want
    message = list_files(folder)

# Save the output to log file
with open("../logs/list_files.log", "a") as log:
    log.write(message)

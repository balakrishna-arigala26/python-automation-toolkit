import re
from datetime import datetime

def run(file):
    try:
        with open(file, "r") as log_file:
            content = log_file.readlines()

        error_warning = [
            line for line in content if re.search(r"(ERROR|WARNING)", line)
        ]

        with open("logs/parsed_errors.log", "a") as output:
            for line in error_warning:
                output.write(line)

        print("\n🔍 Log parsing completed! Check logs/parsed_errors.log\n")

    except FileNotFoundError:
        print(f"❌ Log file not found: {file}")

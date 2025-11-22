import os
import re
from datetime import datetime

LOG_FILE = "../logs/sample.log"  # Source log file for parsing
OUTPUT_FILE = "../logs/parsed_errors.log" # Target log file for results

def parse_logs():
    if not os.path.exists(LOG_FILE):
        print(f"Log file not found: {LOG_FILE}")
        return
    
    pattern_error = r"ERROR.*"
    pattern_warning = r"WARNING.*"

    parsed_lines = []

    with open(LOG_FILE, "r") as log:
        for line in log:
            if re.search(pattern_error, line):
                parsed_lines.append(f"{datetime.now()} | ERROR | {line.strip()}")
            elif re.search(pattern_warning, line):
                parsed_lines.append(f"{datetime.now()} | WARNING | {line.strip()}")

    with open(OUTPUT_FILE, "a") as out_file:
        for item in parsed_lines:
            out_file.write(item + "\n")

    print("Log parsing completed. Check logs/parsed_errors.log")

if __name__ == "__main__":
    parse_logs()
    
import argparse
import json
import os

# Load config.json
CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
with open(CONFIG_PATH, "r") as f:
    cfg = json.load(f)

from scripts.list_files import run as list_files_run
from scripts.file_organizer import run as organize_files_run
from scripts.log_parser import run as parse_logs_run
from scripts.system_monitor import run as system_monitor_run

def main():
    parser = argparse.ArgumentParser(description="Python Automation Toolkit CLI")
    parser.add_argument("command", choices=["list-files", "organize", "parse-logs", "monitor"],
                        help="Choose automation task to run")
    args = parser.parse_args()

    if args.command == "list-files":
        list_files_run(cfg["LIST_FILES_PATH"])

    elif args.command == "organize":
        organize_files_run(cfg["ORGANIZE_FOLDER"])

    elif args.command == "parse-logs":
        parse_logs_run(cfg["LOG_PARSE_FILE"])

    elif args.command == "monitor":
        system_monitor_run(cfg["MONITOR_INTERVAL"])

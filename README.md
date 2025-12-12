🐍 Python Automation Toolkit — DevOps Focus

A production-style Python automation toolkit packaged into a single CLI command — designed for DevOps, SRE, and Production Support workflows.
It automates real engineering tasks such as log parsing, file organization, system monitoring, and directory inspection — with logging, observability, and CI pipeline validation.

📌 Table of Contents

Features

Installation

CLI Usage Examples

Project Structure

Screenshots

Skills Demonstrated

Roadmap

License

🚀 Features
CLI Command Automation Performed
automation-toolkit list-files Lists files & logs output with timestamps
automation-toolkit organize Organizes files into categorized folders
automation-toolkit parse-logs Extracts ERROR & WARNING from logs
automation-toolkit monitor Tracks CPU / Memory / Disk usage with alert logs

Each task logs structured output similar to real DevOps/SRE operational tools.

⚙️ Installation & Setup
1️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate

2️⃣ Install the toolkit in editable mode
pip install -e .

3️⃣ Run the automation using CLI
automation-toolkit list-files
automation-toolkit organize
automation-toolkit parse-logs
automation-toolkit monitor

🧪 CLI Usage Examples
✔ List files
automation-toolkit list-files

Output example:

Listing files in: .

- README.md
- scripts
- logs

✔ Organize files
automation-toolkit organize

Automatically categorizes into:

organized-files/
│── Documents/
│── Images/
│── Others/

✔ Parse logs
automation-toolkit parse-logs

Extracts all ERROR and WARNING lines → saved to:

logs/parsed_errors.log

✔ System monitor
automation-toolkit monitor

Logs CPU / Memory / Disk every interval (defined in config.json).

📁 Project Structure
python-automation-toolkit/
│── automation_toolkit/ → CLI entry module (automation-toolkit command)
│── scripts/ → Automation logic (list, organize, parse, monitor)
│── config.json → Central config for CLI
│── logs/ → Log outputs
│── organized-files/ → File organizer output
│── screenshots/ → Documentation screenshots
│── setup.py → Packaging configuration
│── requirements.txt
│── README.md

📸 Screenshots
🔹 Project Folder Structure

🔹 CI Pipeline Status

🔹 System Monitor Output

🔹 File Organizer Output

🧠 Skills Demonstrated

Python scripting for DevOps automation

Directory and file operations

Log parsing using regex

System monitoring with thresholds

Writing reusable CLI tools using entry points

Logging and timestamping (observability)

GitHub Actions CI pipeline

Git & GitHub workflow

Virtual environments and editable installs

🛣 Roadmap (Upcoming Enhancements)

Publish toolkit to PyPI

Add email/SMS alerts for system monitoring

Add Docker support

Create installer script

Add unit tests + coverage badges

📌 License

This project is for personal learning and practice.

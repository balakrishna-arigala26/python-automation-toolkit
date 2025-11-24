# Python Automation Toolkit

A collection of DevOps-style Python automation scripts for learning and practice real-world automation tasks.

This project demonstrates file handling, directory operations, scripting workflows, and Linux-friendly automation-skills commonly used by DevOps, SRE, and Support Engineers.

---

## Project Structure

```
python-automation-toolkit/
│── scripts/             → All Python automation scripts
│── utils/               → Helper modules (future use)
│── logs/                → Log output files
│── organized-files/     → Output folder for file organizer script
│── README.md            → Documentation

```

---

## Included Automation Scripts

### **1 List Files Script**

Lists all files insisde a specified directory and logs the results with timestamps.

**Run:**

```bash
python3 scripts/list_files.py
```

**Logs saved at:**

````bash
logs/list_files.log

---

### **2 File Organizer Script**
Organizes files by type (Images, Documents, Achives, Scripts, Others) into structured folders.

**Run:**
```bash
python3 scripts/file_organizer.py
````

**Logs stored at:**

```bash
logs/file_organizer.log
```

**Organized output:**

```bash
organized-files/
```

---

### **3 Log Parser Script**

Parses a log file and extracts all **ERROR** and **WARNING** messages using regex.
Useful for monitoring, troubleshooting and automated alerting.

**Run:**

```bash
python3 scripts/log_parser.py
```

**Parsed output stored at:**

```bash
logs/parsed_errors.log
```

---

## Prpose of This Toolkit

This project helps practice automation concepts used in:

- DevOps
- SRE (Site Reliabilty Engineering)
- Production Support
- Python scripting
- Linux system automation
- Git-based workflow

Skills covered:

- File operations
- Directory manipulation
- Log parsing using regex
- Writing clean command-line automation tools
- Git & Github version contol
- Logging & timestamping for observability

---

## How to Run Any Script

From the project root:

```bash
python3 scripts/<script_name>.py
```

Example:

```bash
python3 scripts/log_parser.py
```

---

## Licence

This project is for personal learning and practice.

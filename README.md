# 🐍 Python Automation Toolkit — DevOps Focus

[![CI Status](https://github.com/balakrishna-arigala26/python-automation-toolkit/actions/workflows/python-ci.yml/badge.svg)](https://github.com/balakrishna-arigala26/python-automation-toolkit/actions/workflows/python-ci.yml)

A production-style Python automation toolkit packaged into a **single CLI command** — designed for **DevOps, SRE, and Production Support** workflows.

It automates frequent operational tasks including monitoring, log parsing, file management, and directory organization — with **observability, logging, and CI validation**.

---

## 🚀 Features

| CLI Command                     | Automation Performed                             |
| ------------------------------- | ------------------------------------------------ |
| `automation-toolkit list-files` | Lists files & logs output with timestamps        |
| `automation-toolkit organize`   | Organizes files into categorized folders         |
| `automation-toolkit parse-logs` | Extracts `ERROR` & `WARNING` from logs           |
| `automation-toolkit monitor`    | Tracks CPU / Memory / Disk usage with alert logs |

---

## ⚙️ Installation & Setup

### 1️⃣ Create virtual environment

**Run:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **2️⃣ Install the toolkit in editable mode**

**Run:**

```bash
pip install -e .
```

### **3️⃣ Run automation using CLI**

**Run:**

```bash
automation-toolkit list-files
automation-toolkit organize
automation-toolkit parse-logs
automation-toolkit monitor
```

## 📁 Project Structure

```bash
python-automation-toolkit/
│── automation_toolkit/      → CLI entry module
│── scripts/                 → Automation logic modules
│── config.json              → Central configuration file
│── logs/                    → Log outputs
│── organized-files/         → Output from file organizer
│── screenshots/             → Images for documentation
│── setup.py                 → Packaging configuration
│── requirements.txt
│── README.md
```

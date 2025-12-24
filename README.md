# Python Automation Toolkit

![CI](https://github.com/balakrishna-arigala26/python-automation-toolkit/actions/workflows/ci.yml/badge.svg)

A production-ready **Python automation toolkit** demonstrating real-world DevOps practices:
- clean modular code
- strict linting & formatting
- enforced test coverage
- GitHub Actions CI

This repository follows the same quality gates used in **real production Python / DevOps teams** and is designed as a **portfolio-grade DevOps / Automation Engineer project**.

---

## ✨ Features

- 📁 File organization utilities
- 📄 File listing with filtering
- 📜 Log parsing helpers
- 🖥️ System monitoring utilities
- 🧪 High test coverage (≥ 90%)
- 🧹 Code quality enforced via CI

---

## 📂 Project Structure

```text
python-automation-toolkit/
├── automation_toolkit/
│   ├── cli.py
│   ├── file_organizer.py
│   ├── list_files.py
│   ├── log_parser.py
│   └── system_monitor.py
├── tests/
│   ├── test_file_organizer.py
│   ├── test_list_files.py
│   ├── test_log_parser.py
│   └── test_system_monitor.py
├── .github/workflows/ci.yml
├── pyproject.toml
├── tox.ini
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
└── README.md 

## 🚀 Getting Started (Local)

1️⃣ Clone repository

```bash
git clone https://github.com/balakrishna-arigala26/python-automation-toolkit.git
```

```bash
cd python-automation-toolkit
```

2️⃣ Create virtual environment and activate

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

3️⃣ Install dependencies

```bash
pip install --upgrade pip
```

```bash
pip install -r requirements-dev.txt
```

## 🧪 Run Quality Checks Locally

Format & lint

```bash
isort .
```

```bash
black .
```

```bash
flake8 .
```

Run tests with coverage

```bash
pytest
```

Expected:
  -  ✅ All tests pass

  -  ✅ Coverage ≥ 90%


## 🧪 Run via tox (CI simulation)

```bash
tox
```

## 🤖 Continuous Integration

GitHub Actions runs on every push and pull request:

    - `isort --check-only .`
    - `black --check .`
    - `flake8 .`
    - `pytest` (with coverage gate)

CI fails if:

    - formatting is incorrect
    - linting fails
    - coverage < 90%

📜 License

MIT License
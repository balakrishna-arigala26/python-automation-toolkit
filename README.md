# Python Automation Toolkit


[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![CI](https://github.com/balakrishna-arigala26/python-automation-toolkit/actions/workflows/ci.yml/badge.svg)


A **production-ready Python automation toolkit** demonstrating real-world DevOps practices such as containerization, CI pipelines, and clean project structure.

This project is built to reflect how automation tools are developed, tested, and shipped in real engineering teams.

---

## 🚀 Features

- Modular Python automation utilities
- Clean CLI interface
- Dockerized using multi-stage builds
- Non-root container execution
- GitHub Actions CI pipeline
- Linting, formatting & test enforcement
- Production-style project structure

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
```

## 🐳 Run with Docker

**Build image** 

```bash
docker build -t automation-toolkit . 
```
**Run CLI**

```bash
docker run --rm automation-toolkit --help
```

## 🧪 Local Development

**Setup virtual environment**

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

**Install dependencies**

```bash
pip install --upgrade pip
```

```bash
pip install -r requirements-dev.txt
```

## 🧹 Code Quality Checks

**Format & lint**

```bash
isort .
```

```bash
black .
```

```bash
flake8 .
```

**Run tests with coverage**

```bash
pytest
```

All checks must pass before merging.


## 🧪 Run via tox (CI simulation)

```bash
tox
```

## 🤖 CI Pipeline

GitHub Actions runs on 

- Push to `main`
- Pull requests targetting `main`

Pipeline steps:

- Docker image buuild
- Linting & formatting checks
- Test execution

This ensures consistent, production-ready quality.

## 🗺️ Roadmap

- Push Docker image to AWS ECR
- Deploy container to EC2
- Add monitoring & logs
- Improve CLI UX

## 📄 License

This project is licensed under the MIT License.

→ See [LICENSE](LICENSE)
CI/CD enabled

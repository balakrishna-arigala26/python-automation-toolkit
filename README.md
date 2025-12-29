# Python Automation Toolkit


[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![CI](https://github.com/balakrishna-arigala26/python-automation-toolkit/actions/workflows/ecr-push.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![AWS ECR](https://img.shields.io/badge/AWS-ECR-orange?logo=amazonaws)


A **production-ready Python automation toolkit** demonstrating real-world **DevOps practices**, including containerization, CI/CD automation, and cloud-native workflows using **Docker GitHub Actions, and AWS ECR.**

This project reflect how modernengineering teams **build,test,package,and deleiver** Python applications in real environments.

---

## 🚀 Key Highlights

- Modular and extensible Python automation utilities
- Clean CLI-base architecture
- Dockerized using multi-stage builds
- Secure, non-root container execution
- CI/CD pipeline using GitHub Actions
- Automated Docker image publishing to AWS ECR
- Secure authentication via GitHub OIDC (no secrets stored)
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
├── .github/workflows/
│   └── ecr-push.yml
├── Dockerfile
├── pyproject.toml
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

**Creation and activation of virtual environment**

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

## 🔁 CI/CD Pipeline (GitHub Actions)

This project uses GitHub Actions for Continuous Itegration and Delivery.

**Pipeline includes:**

- Docker image build
- Secure authentication using AWS OIDC
- Image push to AWS ECR
- Versioned image tagging

**Trigger:**

- Every push to the `main` branch

## 🏷️ Image Versioning Strategy

Each build produces:
- `latest` → most recent build
- `<commit-sha>` → immutable,traceable version

Example:

```text
python-automation-toolkit:latest
python-automatio-toolkit:3fa9c2b
```

## ☁️ AWS ECR

Images are pushed automatically to:

```bash
<account-id>.dkr.ecr.ap-south-1.amazonaws.com/python-automation-toolkit
```
Authentication is handled securely using **GitHub OIDC**, without storing AWS credentials.

## 🔐 Security Best Practices

- No static secrets stored in GitHub
- Least-previlege IAM role usage
- Secure image builds
- Reproducible CI pipelines


## 🗺️ Roadmap

- ✅ Dockerized application

- ✅ CI/CD with GitHub Actions

- ✅ AWS ECR integration

- ⏳ Image lifecycle policies

- ⏳ ECS deployment

- ⏳ Observability & logging


## 📄 License

This project is licensed under the **MIT License.**

→ See [LICENSE](LICENSE)

## 🙌 Acknowledgements

Built as part of continuous learning in:

- Python Automation
- DevOps Engineering
- Cloud-Native Development

## 💬 Feedback & Contributions

Suggestions and improvements are welcome!
Feel free to open an issue or start a discussion.

## ⭐ If you found this useful, consider starring the repository!
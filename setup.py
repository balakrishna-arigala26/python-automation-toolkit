from setuptools import find_packages, setup

setup(
    name="automation-toolkit",
    version="0.1.0",
    description="DevOps-focused Python automation toolkit",
    packages=find_packages(),
    install_reuires=[
        "click>=8.0",
    ],
    entry_point={
        "console_scripts": [
            "automation-toolkit=automation_toolkit.cli:cli",
        ],
    },
)

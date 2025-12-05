from setuptools import setup, find_packages

setup(
    name="python-automation-toolkit-balu",
    version="1.0.0",
    description="A learning-oriented DeOps-style Python automation toolkit",
    packages=find_packages(exclude=["venv", "screenshots"]),
    include_package_data=True,
    install_requires=[
        "psutils",
    ],
    entry_points={
        "console_scripts": [
            "automation-toolkit=automation_toolkit.cli:main",
        ],
    },
)



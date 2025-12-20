from setuptools import setup, find_packages

setup(
    name="cli-tool",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.1.7",
        "rich>=13.7.0",
        "python-dotenv>=1.0.1",
        "pyyaml>=6.0.1",
    ],
    entry_points={
        "console_scripts": [
            "mytool=src.cli:main",
        ],
    },
    python_requires=">=3.8",
)

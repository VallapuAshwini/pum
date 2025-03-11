from setuptools import setup, find_packages

setup(
    name="pubmed_papers",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "get-papers-list=pubmed_papers.cli:main",
        ],
    },
)

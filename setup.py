from setuptools import setup, find_packages

setup(
    name="branch-pruner",
    version="0.0.1",
    author="Dedar Alam",
    author_email="devded@pm.me",
    url="https://github.com/devded/branch-pruner",
    description="Remove unecessary branches from git repository",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["branch-pruner = src.main:main"]},
)
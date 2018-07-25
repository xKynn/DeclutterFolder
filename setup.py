from setuptools import setup

with open("README.md") as f:
    desc = f.read()

setup(
    name = 'declutter',
    version = '0.1',
    packages = ['declutter'],
    author = "xKynn",
    description = "A commandline utility to declutter the files in current directory by organizing into folders automatically.",
    long_description=desc,
    long_description_content_type="text/markdown",
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points = {
        'console_scripts': [
            'declutter = declutter.__main__:main'
        ]
    })
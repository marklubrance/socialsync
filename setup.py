from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="socialsync",
    version="1.0.1",
    author="Mark Lubrance",
    author_email="socialsync.software@outlook.com",
    description="A powerful Python library for automating interactions with social media platforms and integrating them with backend systems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.1",
        "hashlib>=1.0.1",
        "typing_extensions>=4.0.0",
        "pytest>=7.0.0",
        "flake8>=5.0.0",
        "black>=23.0.0",
        "pandas>=1.3.0",
        "aiohttp>=3.8.0",
        "cryptography>=3.0.0",
    ],
    classifiers = [
        "Typing :: Typed",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License"
    ],
    python_requires=">=3.8",
)
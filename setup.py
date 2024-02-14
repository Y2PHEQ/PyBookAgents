import pathlib
from setuptools import setup
from setuptools import find_packages

PACKAGE = "PyBookAgents"
THIS_DIR = pathlib.Path(__file__).parent
LONG_DESCRIPTION = (THIS_DIR / "README.md").read_text()

setup(
    name=PACKAGE,
    version='0.0.2',
    description="Random user agents generator for Facebook. It has 4 options: Dalvik, iPhone, Android, and Random (it's either Android or iPhone).",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Sintacs Ao",
    author_email="sintacs@isnotdev.com",
    license="MIT",
    url="https://facebook.com/sintxcs",
    zip_safe=False,
    project_urls={"GitHub": "https://github.com/sintxcs"},
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    #setup_requires=["wheel"],
    #python_requires='>=3.7'
)

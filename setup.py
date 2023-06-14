import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="addnum",
    version="1.0.0",
    description="add numbers",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hustlemaniac/addnum",
    author="Add numbers",
    author_email="bhavyasaikamasamudram@gmail.com",
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GPL-3.0 License",
        "Programming Language :: Python :: 3",
    ],
    py_modules=["addnum"],
    entry_points={"console_scripts": ["addnum=addnum:main"]},
)
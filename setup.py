import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="tensorboard_jhm",
    version="1.0.0",
    description="Jupyter notebook magic to open frames with jupyter_tensorboard.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/poiug07/tensorboard_jhm",
    author="Kozhin Assan",
    license="MIT",
    classifiers=[
        "Framework :: IPython",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],    
    packages=["tensorboard_jhm"],
    include_package_data=True,
    install_requires=[
        "notebook",
    ],
)
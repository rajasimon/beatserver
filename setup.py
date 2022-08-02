from setuptools import setup, find_packages
from beatserver import __version__


def get_long_description():
    """
    Return the README.
    """
    with open("README.md", encoding="utf8") as f:
        return f.read()


setup(
    name="beatserver",
    version=__version__,
    url="https://github.com/rajasimon/beatserver",
    author="Raja Simon",
    author_email="rajasimon@icloud.com",
    description="Beat Server is is a scheduler",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    install_requires=["channels>=1.1.8.1", "croniter>=0.3.30"],
    include_package_data=True,
)

from setuptools import setup, find_packages
from beatserver import __version__


setup(
    name="beatserver",
    version=__version__,
    url="https://github.com/rajasimon/beatserver",
    author='Raja Simon',
    author_email='rajasimon@icloud.com',
    description="Beat Server is is a scheduler",
    license='MIT',
    packages=find_packages(),
    install_requires=['channels>=1.1.8.1', 'croniter>=0.3.30'],
    include_package_data=True

)

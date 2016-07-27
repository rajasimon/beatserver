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
    install_requires=['django', 'channels'],
    include_package_data=True,
    entry_points={'console_scripts': [
        'beatserver = beatserver.cli:CommandLineInterface.entrypoint',
    ]},

)

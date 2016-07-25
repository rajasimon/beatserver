from setuptools import setup, find_packages
from beatserver import __version__


setup(
    name="beatserver",
    version=__version__,
    url="https://github.com/rajasimon/beatserver",
    description="Beat Server",
    license='MIT',
    packages=find_packages(),
    install_requires=['django', 'channels'],
    include_package_data=True,
    entry_points={'console_scripts': [
        'beatserver = beatserver.cli:CommandLineInterface.entrypoint',
    ]},

)

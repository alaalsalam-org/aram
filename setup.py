from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in aram/__init__.py
from aram import __version__ as version

setup(
	name="aram",
	version=version,
	description="aram",
	author="nsfss",
	author_email="Ezzat.orc@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

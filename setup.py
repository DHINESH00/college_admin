from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in college_admissions/__init__.py
from college_admissions import __version__ as version

setup(
	name="college_admissions",
	version=version,
	description="in this application we are going to create a new college new student in which you can help the student to enroll a particular college in a particular semester",
	author="dhinesh",
	author_email="dhinesh200014@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

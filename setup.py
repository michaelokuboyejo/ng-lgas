import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='ng-lgas',
    packages=['ng-lgas'],
    version='0.1',
    description='A Python Library that offers a list of local government areas in Nigeria as well as their coordinates (latitudes and longitudes).',
    author='Michael Okuboyejo',
    author_email='mykelokuboyejo@gmail.com',
    url='https://github.com/michaelokuboyejo/ng-lgas',
    download_url='https://github.com/michaelokuboyejo/ng-lgas/tarball/0.1',
    keywords=['ng-lgas', 'local government areas', 'nigeria'],
    classifiers=[],
)

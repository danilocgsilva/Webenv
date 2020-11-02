from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="www_local_finder_cli",
    version=VERSION,
    description="Command line to track some properties from current environment for web development",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="web development",
    url="https://github.com/danilocgsilva/www_local_finder_cli",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["www_local_finder_cli"],
    entry_points={"console_scripts": ["envweb=www_local_finder_cli.__main__:main"],},
    include_package_data=True
)


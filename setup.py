from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="Endpoints Manager",
    version=VERSION,
    description="Facilitates the work of managing several access data for an web application",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="manage environment connections endpoints services",
    url="https://github.com/danilocgsilva/endpoints_manager",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["endpoints_manager"],
    entry_points={"console_scripts": ["envm=endpoints_manager.__main__:main"],},
    include_package_data=True
)


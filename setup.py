import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyfilemaker',
    version='0.0.1.1',
    author='Marcus Evans',
    author_email='marcus@marcusbevans.com',
    description='Python library for FileMaker JDBC Driver',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/caeneb/pyfilemaker',
    project_urls={
        "Bug Tracker": "https://github.com/caeneb/pyfilemaker/issues"
    },
    license='MIT',
    packages=['pyfm'],
    install_requires=['jaydebeapi'],
)

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cnfilemaker',
    version='0.0.1.7',
    author='Marcus Evans',
    author_email='marcus@marcusbevans.com',
    description='Python library for FileMaker JDBC/ODBC Driver',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/caeneb/cnfilemaker',
    project_urls={
        "Bug Tracker": "https://github.com/caeneb/cnfilemaker/issues"
    },
    license='MIT',
    packages=['cnfilemaker'],
    install_requires=['jaydebeapi'],
)

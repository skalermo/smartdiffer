from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

VERSION = '0.1.3'
DESCRIPTION = 'Tool to compare smart contracts source code'

setup(
    name="smartdiffer",
    version=VERSION,
    author="skalermo (Roman Moskalenko)",
    author_email="skalermo@gmail.com",
    description=DESCRIPTION, 
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=find_packages(),
    install_requires=[
        'requests>=2.26.0',
        'py-etherscan-api>=0.8.0',
    ],
    keywords=['python', 'etherscan-api', 'diffchecker'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    url='https://github.com/skalermo/morphine',
    entry_points={
        'console_scripts': [
            'smartdiffer=smartdiffer.cli:main',
        ],
    },
)

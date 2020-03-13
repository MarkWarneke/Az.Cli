import setuptools

VERSION = "0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

setuptools.setup(
    name="az.cli",
    version=VERSION,
    author="Mark Warneke",
    author_email="warneke.mark@gmail.com",
    classifiers=CLASSIFIERS,
    description="An interface to execute Azure CLI commands using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkWarneke/Az.Cli",
    packages=['az'],
    package_dir={'az': 'src/az'},
    python_requires='>=3.7',
    install_requires=required,
)

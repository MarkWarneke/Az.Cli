import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('REQUIREMENTS.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="az.cli",
    version="0.1",
    author="Mark Warneke",
    author_email="warneke.mark@gmail.com",
    description="An interface to execute Azure CLI commands using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkWarneke/Az.Cli",
    packages=['az'],
    package_dir={'az': 'src/az'},
    python_requires='>=3.7',
    install_requires=required,
)

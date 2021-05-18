import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pipelines",
    version="1.0.0",
    author="adamnpeace",
    author_email="test@email.com",
    description="Pipelines for T5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamnpeace/question-generation",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
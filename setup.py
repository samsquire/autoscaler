import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws-autoscaler",
    version="0.0.3",
    author="Samuel Michael Squire",
    author_email="sam@samsquire.com",
    description="A simple autoscaler for AWS for use with HAProxy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samsquire/autoscaler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['aws_autoscaler/bin/autoscaler'],
    include_package_data=True
)

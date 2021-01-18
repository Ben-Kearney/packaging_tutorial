import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="package_test",
    version="0.0.2",
    author="bkearney",
    author_email="bkearney@intelcomexpress.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'python_hello@git+https://github.com/ceddlyburge/python_hello#egg=python_hello',
        'boto3==1.14.53',
    ]
)
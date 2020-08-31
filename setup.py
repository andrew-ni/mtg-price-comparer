import setuptools

setuptools.setup(
    name="mtg-price-comparer",
    version="0.0.1",
    author="Andrew Ni",
    author_email="niandrewdev@gmail.com",
    description="Compares prices between TCG Player and Card Kingdom",
    long_description_content_type="text/markdown",
    url="https://github.com/andrew-ni/mtg-price-comparer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

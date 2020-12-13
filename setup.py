import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt') as fr:
    reqs = fr.read().strip().split('\n')


setuptools.setup(
    name="maskoff",
    version="0.0.1",
    author="Minsu Park",
    author_email="santaonchair@gmail.com",
    description="Mask off Be happy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/santaonchair/maskoff",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=reqs,
)

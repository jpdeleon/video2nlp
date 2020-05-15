import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name="vido2nlp",
    version="0.1.1",
    author="Jerome de Leon",
    author_email="jpdeleon.bsap@gmail.com",
    description="NLP of closed caption (cc) of youtube videos",
    long_description=long_description,
    url="https://github.com/jpdeleon/video2nlp",
    packages=setuptools.find_packages(exclude=["tests"]),
    # package_data={"craigslist": ["data/*"]},
    # include_package_data=True,
    scripts=["video2nlp.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
)

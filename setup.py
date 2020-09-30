import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="buy_lambo",
    version="0.1.0",
    author="Napoleon-Christos Oikonomou",
    author_email="napoleonoikon@gmail.com",
    description="Scripts to create a BTC address whose assets are locked until a specified time (or block) and after that time, transfer all funds to another address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamnapo/buy-lambo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "bitcoin_utils>=0.4.10,<0.5",
        "requests==2.24.0,<3",
        "python-dotenv==0.14.0,<0.15",
    ],
    scripts=["bin/buy_lambo", "bin/create_HODL_address"],
    keywords="bitcoin btc p2sh lambo timelock p2pkh",
    license="MIT",
    include_package_data=True,
)

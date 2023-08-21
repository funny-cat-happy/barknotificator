from setuptools import setup, find_packages

VERSION = "0.1.1"
DESCRIPTION = "A package that allows you to send notifications to your iOS device using the Bark app without self server"
long_description = (
    "For details, please visit the https://github.com/funny-cat-happy/barknotificator"
)


setup(
    name="barknotificator",
    version=VERSION,
    author="funny-cat-happy",
    author_email="tigerhowl@qq.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["httpx[http2]", "pyjwt", "cryptography"],
    keywords=["bark", "notification", "iOS", "barknotificator"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires=">=3",
)

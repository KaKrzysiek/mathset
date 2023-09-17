from distutils.core import setup

setup(
    name = "mathset",
    packages = ["mathset"],
    version = "1.0.1",
    license = "mpl-2.0",
    description = "mathset is a Python module allowing user to perform basic mathematical operations on finite sets",
    author = "Krzysztof Karczewski",
    author_email = "kakrzysiek13@gmail.com",
    download_url = "https://github.com/KaKrzysiek/mathset/archive/refs/tags/v_1.0.1.tar.gz",
    keywords = ["mathset", "MathSet", "Python Programming Language", "open source", "set", "mathematics"],
    install_requires = ["typing"],
    classifiers = [
        "Programming Language :: Python :: 3",
	    "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
	    "Operating System :: OS Independent"]
)

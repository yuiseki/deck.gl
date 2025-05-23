from os.path import join
from setuptools import find_packages, setup

version_ns = {}
with open(join("pydeck_carto", "_version.py")) as f:
    exec(f.read(), {}, version_ns)

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pydeck-carto",
    version=version_ns["__version__"],
    description="Pydeck wrapper for use with CARTO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["pydeck", "carto", "visualization", "graphics", "GIS", "maps"],
    author="CARTO",
    author_email="jarroyo@carto.com",
    url="https://github.com/visgl/deck.gl/tree/master/bindings/pydeck-carto",
    license="BSD 3-Clause",
    packages=find_packages(exclude=["examples", "tests"]),
    python_requires=">=3.8",
    install_requires=[
        "pydeck>=0.9.0",
        "carto-auth>=0.2.0",
        "typing-extensions>=4.0.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Jupyter",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    zip_safe=False,
)

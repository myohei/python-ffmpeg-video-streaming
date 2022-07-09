from setuptools import setup, find_packages

setup(
    name="ffmpeg-streaming",
    packages=find_packages(exclude=('tests*',)),
    version="0.1.16",
    # install_requires=[],
    entry_points={}
)

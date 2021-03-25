
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flask_minio_factory",
    version="0.1.2",
    author="",
    author_email="",
    description="A package, which provides easy usage for minio with flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'minio'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'dev': [
            'Flask',
            'pytest',
            'coveralls',
            'coverage'
        ],
    }
)

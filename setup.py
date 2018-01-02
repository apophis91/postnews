from setuptools import setup, find_packages

setup(
    name="postnews",
    description="Basic flask Api",
    version="0.1",
    author="RAR",
    packages=[
        "postnews",
    ],
    include_package_data=True,
    install_requires=[
        "flask>0.12",
        "flask-sqlalchemy>2.3",
        "flask-HTTPAuth"
    ]
)

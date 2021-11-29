from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip() 
        for req 
        in open(filename).readlines()
        ]

setup(
    name="pokedexN2t",
    version="0.1.0",
    description="pokedex test",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)
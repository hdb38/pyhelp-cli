from setuptools import setup, find_packages

setup(
    name="pyhelp",
    version="8.0.0",
    py_modules=find_packages(),
    install_requires=["click","flask","numpy"],
    entry_points={
        "console_scripts": [
            "pyhelp=pyhelp:cli"
        ]
    }
)
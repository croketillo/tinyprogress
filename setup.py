from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tinyprogress",  # Cambia esto por el nombre de tu paquete
    version="1.1.0",
    author="Croketillo",
    author_email="croketillo@gmail.com",
    description="A lightweight progress bar for Python without dependencies.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/croketillo/tinyprogress",  # Cambia por la URL de tu repositorio
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules', 
        'Topic :: Utilities'
    ],
    python_requires='>=3.6',
)

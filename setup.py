# This file were created by Python Boilerplate. Use Python Boilerplate to start
# simple, usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/
#

import os

from setuptools import setup, find_packages, find_namespace_packages

# Meta information
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)

setup(
    name='calc42',
    version=version,
    author='Marián Lorinc',
    author_email='xlorin01@vutbr.cz',
    url='',
    description='A minimalistic calculator',
    long_description=open('README.md').read(),
    classifiers=[
        'License :: OSI Approved :: GNU General Public License ver. 3 (GPL3)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],

    # Packages and dependencies
    # package_dir={'': 'src'},
    packages=find_packages(exclude=("tests",)),

    install_requires=[
        "PySide2"
    ],
    extras_require={
        'dev': [
            'sphinx',
            "recommonmark",
            "sphinx-intl"
        ],
    },

    # Data files
    package_data={
        'resources': ["*.css,", "*.mo", "*.desktop"]
    },

    include_package_data=True,

    # Scripts
    entry_points={
        'gui_scripts': [
            'calc42 = ptr42.main:main'],
    },

    # Other configurations
    zip_safe=False,
    platforms='any',
)

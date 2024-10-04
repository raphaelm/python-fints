from codecs import open
from os import path

from fints import version
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

try:
    # Get the long description from the relevant file
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

setup(
    name='fints',
    version=version,
    description='Pure-python FinTS 3.0 (formerly known as HBCI) implementation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/raphaelm/python-fints',
    author='Raphael Michel',
    author_email='mail@raphaelmichel.de',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],

    keywords='hbci banking fints',
    install_requires=[
        'bleach',
        'mt-940',
        'requests',
        'sepaxml~=2.1',
        'enum-tools~=0.12.0',
    ],

    packages=find_packages(include=['fints', 'fints.*']),
)

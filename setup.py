import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

long_description = read('README.md')

install_requires = [
    'appdirs',
    'asks',
    'trio'
]

tests_require = [
    'pytest',
    'asynctest',
    'coverage',
    'pytest-cov',
    'pytest-mock',
    'pytest-trio',
]


def read_version():
    for line in open(os.path.join('ncbi_genome_download', '__init__.py'), 'r'):
        if line.startswith('__version__'):
            return line.split('=')[-1].strip().strip("'")


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='ncbi-genome-download',
    version=read_version(),
    author='Kai Blin',
    author_email='kblin@biosustain.dtu.dk',
    description='Download genome files from the NCBI FTP server.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    entry_points={
        'console_scripts': [
            'ncbi-genome-download=ncbi_genome_download.__main__:main',
            'ngd=ncbi_genome_download.__main__:main'
        ],
    },
    packages=['ncbi_genome_download'],
    url='https://github.com/kblin/ncbi-genome-download/',
    license='Apache Software License',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    extras_require={
        'testing': tests_require,
    },
)

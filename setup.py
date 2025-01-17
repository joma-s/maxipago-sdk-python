# coding: utf-8
import re
import os
from setuptools import setup, find_packages
from codecs import open



def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    meta_filedata = read_file('maxipago/__init__.py')
    re_version = re.compile(r'VERSION\s*=\s*\((.*?)\)')
    group = re_version.search(meta_filedata).group(1)
    version = filter(None, map(lambda s: s.strip(), group.split(',')))
    return '.'.join(version)


setup(
    name='maxipago-sdk',
    version=get_version(),
    author='Stored',
    author_email='contato@stored.com.br',
    description='SDK Python for Maxipago',
    license='MIT',
    keywords='',
    url='https://github.com/joma-s/maxipago-sdk-python',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    long_description=read_file('README.md'),
    classifiers=[
        "Topic :: Utilities",
    ],
    install_requires=[
        'requests>=2.22.0',
        'lxml>=4.6.4',
        'pyOpenSSL>=18.0.0'
    ],
)

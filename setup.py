# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='benchmark-places',
    version='0.0.1',
    author=u'Ken Koontz',
    author_email='kenneth.koontz@gmail.com',
    packages=find_packages(),
    license='MIT licence, see LICENCE.txt',
    url='https://github.com/usebenchmark/benchmarkplaces.git',
    description='Place abstraction',
    long_description=open('README.md').read(),
    install_requires = [
        'rauth',
        'requests'
    ],
    zip_safe=False,
)

# url='http://bitbucket.org/bruno/django-geoportail',

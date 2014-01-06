#!/usr/bin/env python
from distutils.core import setup

# Use quickphotos.VERSION for version numbers
version_tuple = __import__('quickphotos').VERSION
version = '.'.join([str(v) for v in version_tuple])

setup(
    name='django-quick-photos',
    version=version,
    description='Latest Photos from Instagram for Django',
    long_description=open('README.rst').read(),
    url='https://github.com/blancltd/django-quick-photos',
    maintainer='Alex Tomkins',
    maintainer_email='alex@blanc.ltd.uk',
    platforms=['any'],
    install_requires=[
        'python-instagram>=0.8.0',
    ],
    packages=[
        'quickphotos',
        'quickphotos.management',
        'quickphotos.management.commands',
        'quickphotos.templatetags',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    license='BSD-2',
)

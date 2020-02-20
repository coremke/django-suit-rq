import os

from codecs import open
from setuptools import setup

import suit_rq

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-suit-rq',
    version=suit_rq.__version__,
    author='Ryan Senkbeil',
    author_email='ryan.senkbeil@gsdesign.com',
    description='Support the django-rq admin when using django-suit',
    long_description=long_description,
    url='https://github.com/gsmke/django-suit-rq',
    license='BSD',
    packages=['suit_rq'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'django-suit >=0.2.15, <0.3.0',
        'django-rq >=2.0.2, <3.0.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

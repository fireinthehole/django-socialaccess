import os
from setuptools import setup, find_packages


version = '0.9.3'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'django-socialaccess',
    version = version,
    url = 'http://github.com/fireinthehole/django-socialaccess',
    license = 'BSD',
    description = 'Django client for oauth2 profiders',
    long_description = read('README.rst'),
    author = 'Damian Daskalov',
    author_email = 'daskalov.damian@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'Django>=1.9',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

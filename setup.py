import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-socialaccess",
    version = "0.9",
    url = 'http://github.com/fireinthehole/django-socialaccess',
    license = 'BSD',
    description = 'Django application for cross-site authentications and api access '\
                  'on famous social networks',
    long_description = read('README.rst'),
    author = 'Damian Daskalov',
    author_email = 'daskalov.damian@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'Django>=1.9',
        'oauth2==1.9.0.post1',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

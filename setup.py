import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-socialaccess",
    version = "1.0",
    url = 'http://github.com/fireinthehole/django-socialaccess',
    license = 'BSD',
    description = 'Django application for cross-site authentication and api access '\
                  'on famous social networks based on the python oauth2 lib',
    long_description = read('README.rst'),
    author = 'Damian Daskalov',
    author_email = 'daskalov.damian@gmail.com',
    packages = find_packages(),
    package_data = {'socialaccess': ['templates/socialaccess/*/*']},
    install_requires = [
        'Django>=1.8',
        'oauth2==1.5.211',
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

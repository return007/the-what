import os
from setuptools import setup


README_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'README.md')
)
with open(README_PATH) as f:
    README_DATA = f.read()


# This call to setup() does all the work
setup(
    name                          = 'theWHAT-server',
    version                       = '0.0.1',
    description                   = 'Server that powers theWHAT',
    long_description              = README_DATA,
    long_description_content_type = 'text/markdown',
    url                           = 'https://github.com/return007/the-what',
    author                        = 'return007',
    author_email                  = 'glalchandanig@gmail.com',
    packages                      = ['thewhat'],
    include_package_data          = True,
    python_requires               = '>=3.8',
    license                       = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Programming Language :: Python :: 3',
    ],
    install_requires = [
        'flask',
        'lxml',
    ],
    entry_points = {
        'console_scripts': [
            'thewhat-server=thewhat.app:main',
        ]
    },
)

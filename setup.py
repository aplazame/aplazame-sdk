import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    """
    Usage:
    python setup.py test -a "--host=:host --private-token=:token"
    """
    user_options = [
        ('pytest-args=', 'a', "Arguments to pass to py.test")
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='aplazame-sdk',
    version='0.1.2',
    author='calvin',
    author_email='dani@aplazame.com',
    packages=['aplazame_sdk'],
    scripts=[],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    zip_safe=False,
    url='https://github.com/aplazame/aplazame-sdk',
    license='Apache Software License',
    description='Python Interface to the Aplazame API',
    install_requires=['requests>=1.1.0'],
    dependency_links=[
        'https://github.com/kennethreitz/requests'],
    classifiers=[
        'Programming Language :: Python',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='python aplazame rest sdk',
)

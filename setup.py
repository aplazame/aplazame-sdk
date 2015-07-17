from setuptools import setup


setup(
    name='aplazame-sdk',
    version='0.1.2',
    author='calvin',
    author_email='dani@aplazame.com',
    packages=['aplazame_sdk'],
    scripts=[],
    test_suite='tests',
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

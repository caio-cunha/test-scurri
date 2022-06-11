from setuptools import find_packages, setup

setup(

    name='uk-postcode-validator',
    packages=find_packages(include=['postcode']),
    version='0.1.0',
    description='Lib for validate and formate postcode',
    author='Caio Henrique',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)
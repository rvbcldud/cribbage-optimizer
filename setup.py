from setuptools import setup

setup(
    name = 'Cribbage Hand Optimizer',
    version = '1.0',
    description = 'Chooses the optimal cribbage hand given a dealt hand',
    author = 'Ryan Vanden Bos',
    install_requires = ['numpy'],
    packages = ['cribbage'],
    entry_points={
        'console_scripts': ['cribbage-opt=cribbage.command_line:main']
    }
)
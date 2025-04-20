from setuptools import setup

setup(
    name='csv2md',
    version='0.1',
    packages=['csv2md'],
    entry_points={
        'console_scripts': [
            'csv2md=csv2md.cli:main',
        ],
    },
)

import setuptools
from distutils.core import setup

setup(
    name='api_888_interview',
    version='1.0',
    packages=setuptools.find_packages(),
    url='https://github.com/lfdivino/888-spectate-interview-project',
    author='Luiz Felipe do Divino',
    author_email='lf.divino@gmail.com',
    description='API to consume external data to save new events '
                'and support consults for the matches details',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ]
)
from setuptools import setup, find_packages


setup(
    name='pyjones',
    version='0.1.0',
    description='The ultimate package for calculating light polarizations',
    author='Nicolas Tolazzi',
    author_email='nicolas.tolazzi@googlemail.com',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['numpy']
)

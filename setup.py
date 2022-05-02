from setuptools import setup

setup(
    name='openligadb',
    version='0.1.',
    packages=['tests', 'openligadb'],
    url='',
    license='MIT ',
    author='Daniel Pleus',
    author_email='danielpleus@gmail.com',
    description='Wrapper for the OpenLigaDB API.',
    install_requires = ["pandas", "requests"]
)

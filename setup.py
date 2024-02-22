from setuptools  import setup, find_packages

setup(
    name = 'mypackage',
    version = '0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package_name>',
    author='Your name',
    author_email='<Your Email Address>'
)
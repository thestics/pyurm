from setuptools import find_packages, setup

setup(
    name='urm',
    packages=find_packages(),
    install_requires=[],
    version='0.1.0',
    description='Compile and execute URM programs',
    author='Danylo Kovalenko danil130999@gmail.com',
    license='MIT',
    entry_points={"console_scripts": ["pyurm=urm.__main__:main"]}
)

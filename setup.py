from setuptools import setup

setup(
   name='ClimatExPrep',
   version='0.1.0',
   author='Nic Annau',
   author_email='nicannau@gmail.com ',
   packages=['ClimatExPrep'],
   license='LICENSE',
   description='Python module to to pre-process ClimatEx deep learning data.',
   long_description=open('README.md').read(),
   install_requires=[
         "numpy",
         "matplotlib",
         "scipy",
         "xarray",
         ],
)

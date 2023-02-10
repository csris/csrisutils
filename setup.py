from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='csrisutils',
      version='0.1',
      description='A collection of various tools that I use',
      long_description=readme(),
      url='https://github.com/csris/csrisutils',
      packages=find_packages(
          include=['csrisutils*']
      ),
      zip_safe=False,
      install_requires=[
          'argh'
      ],
      entry_points={
          'console_scripts': [
              'csv = csrisutils.cmd.csv:main',
          ]
      })

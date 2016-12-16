from setuptools import setup

setup(name='winpath',
      version='0.1',
      description='Gets the Bash Ubuntu path of a Windows file/folder',
      url='https://github.com/bernizt/winpath',
      author='Bernat Zaragoza Travieso',
      author_email='bernat.zaragoza.travieso@outlook.com ',
      license='MIT',
      packages=['winpath'],
      scripts=['bin/wp'],
      zip_safe=False)
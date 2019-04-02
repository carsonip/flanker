# coding:utf-8

from setuptools import setup, find_packages


setup(name='flanker',
      version='11.6.13',
      description='Mailgun Parsing Tools',
      long_description=open('README.rst').read(),
      classifiers=[],
      keywords='',
      author='Mailgun Inc.',
      author_email='admin@mailgunhq.com',
      url='http://mailgun.net',
      license='Apache 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      tests_require=[
          'nose',
          'mock'
      ],
      install_requires=[
          'chardet>=1.0.1',
          'cchardet>=0.3.5',
          'cryptography>=0.5',
          'dnsq>=1.1.6',
          'expiringdict>=1.1.2',
          'idna>=2.5',
          'ply>=3.10',
          'redis>=2.7.1',
          'WebOb>=0.9.8'],
)

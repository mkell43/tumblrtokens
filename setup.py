from setuptools import setup

setup(name='tumblrtokens',
      version='0.1',
      description='Abstracts out creating Oauth authentication tokens for Tumblr.',
      url='',
      author='Michael Keller',
      author_email='mike.k@blu-web.com',
      license='MIT',
      packages=['tumblrtokens'],
      install_requires=['oauth2'],
      zip_safe=False)
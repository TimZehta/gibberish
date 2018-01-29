# vim: set fileencoding=utf-8 :

"""glarg setup
"""

# Standard library
from __future__ import absolute_import, division, print_function
import os

# Third-party
from setuptools import setup


setup_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(setup_path, "README.rst"), "rb") as f:
    long_description = f.read().decode("utf-8")
classifiers = ["License :: OSI Approved :: MIT License",
               "Natural Language :: English",
               "Operating System :: POSIX :: Linux",
               "Programming Language :: Python :: 2",
               "Programming Language :: Python :: 2.7",
               "Programming Language :: Python :: 3",
               "Programming Language :: Python :: 3.4",
               "Programming Language :: Python :: 3.5",
               "Programming Language :: Python :: 3.6",
               "Programming Language :: Python :: Implementation :: CPython"]


setup(author='Timid Robot Zehta',
      author_email='tim@zehta.me',
      classifiers=classifiers,
      description="A pseudo-word passphrase generator",
      download_url="https://github.com/TimZehta/glarg/releases",
      entry_points={'console_scripts': 'glarg = glarg:console_main'},
      keywords=["easy", "memorable", "passphrase", "password", "pseudo-word"],
      license='MIT License',
      long_description=long_description,
      name='Glarg',
      py_modules=('glarg',),
      url='https://github.com/TimZehta/glarg',
      version='0.2',
      )

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

setup(name='Glarg',
      description="A pseudo-word generator",
      version='0.2',
      author='Timid Robot Zehta',
      author_email='tim@zehta.me',
      url='https://github.com/TimZehta/glarg',
      py_modules=('glarg',),
      license='MIT License',
      long_description=long_description,
      entry_points={'console_scripts': 'glarg = glarg:console_main'},
      )

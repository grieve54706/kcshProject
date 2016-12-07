#!/usr/bin/env python

from setuptools import setup

setup(name='kcsh',
      version='1.0',
      description='KanColle Shell',
      author='Grieve',
      author_email='grieve54706@gmail.com',
      url='https://github.com/grieve54706/kcshProject',
      packages=['kcsh', 'kcsh.builtins'],
      entry_points="""
      [console_scripts]
      kcsh = kcsh.shell:main
      """,
      )

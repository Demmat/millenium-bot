#!/usr/bin/python
# -*- coding: UTF-8 -*-
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')


Exclusion = ['pdb','unittest','difflib','inspect','doctest', ]



setup(windows=[{
    'script':'update.py',
    'icon_resources':[(1, '..\\ico\\update.ico')]
}],
    options={'py2exe': {'bundle_files': 1,'excludes':Exclusion}},
    zipfile = None,
)


#setup(windows=[{
#    'script':'HttpProxy_Build.py',
#    'icon_resources':[(1, 'wow.ico')]
#}])    


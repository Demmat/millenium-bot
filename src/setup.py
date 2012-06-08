#!/usr/bin/python
# -*- coding: UTF-8 -*-
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')




setup(console=['.\\config.py'])
setup(console=['.\\vote.py'])

setup(windows=[{
    'script':'launch.py',
    'icon_resources':[(1, 'wow.ico')]
}])

#setup(windows=[{
#    'script':'HttpProxy_Build.py',
#    'icon_resources':[(1, 'wow.ico')]
#}])


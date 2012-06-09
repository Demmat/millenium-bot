#!/usr/bin/python
# -*- coding: UTF-8 -*-
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')




#setup(console=['.\\config.py'])
setup(console=[{
    'script':'config.py',
    'icon_resources':[(1, '.\\ico\\cfg.ico')]
}])

setup(console=[{
    'script':'vote.py',
    'icon_resources':[(1, '.\\ico\\tri.ico')]
}])

setup(windows=[{
    'script':'launch.py',
    'icon_resources':[(1, '.\\ico\\wow.ico')]
}])
setup(windows=[{
    'script':'svote.py',
    'icon_resources':[(1, '.\\ico\\gf.ico')]
}])

#setup(windows=[{
#    'script':'HttpProxy_Build.py',
#    'icon_resources':[(1, 'wow.ico')]
#}])


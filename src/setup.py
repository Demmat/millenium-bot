#!/usr/bin/python
# -*- coding: UTF-8 -*-
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')




#setup(console=['.\\config.py'])
setup(console=[{
    'script':'config.py',
    'icon_resources':[(1, '.\\ico\\cfg.ico')]
}],
    options={'py2exe': {'bundle_files': 1}},
    zipfile=None,)

setup(console=[{
    'script':'vote.py',
    'icon_resources':[(1, '.\\ico\\tri.ico')]
}],
    options={'py2exe': {'bundle_files': 1}},
    zipfile=None,)

setup(windows=[{
    'script':'launch.py',
    'icon_resources':[(1, '.\\ico\\wow.ico')]
}],
    options={'py2exe': {'bundle_files': 1}},
    zipfile=None,)
setup(windows=[{
    'script':'svote.py',
    'icon_resources':[(1, '.\\ico\\gf.ico')]
}],
    options={'py2exe': {'bundle_files': 1}},
    zipfile=None,)

setup(console=[{
    'script':'HttpProxy.py',
    'icon_resources':[(1, '.\\ico\\in.ico')]
}],
    options={'py2exe': {'bundle_files': 1}},
    zipfile=None,)

setup(windows=[{
    'script':'xlsRead.py',
    'icon_resources':[(1, '.\\ico\\plus.ico')]
}],
    options={'py2exe': {'bundle_files': 1}},
    zipfile=None,)


setup(windows=[{
    'script':'proxyVote.py',
    'icon_resources':[(1, '.\\ico\\tor1.ico')]
}],
    options={'py2exe': {'bundle_files': 1}},
    zipfile=None,)


#setup(windows=[{
#    'script':'HttpProxy_Build.py',
#    'icon_resources':[(1, 'wow.ico')]
#}])


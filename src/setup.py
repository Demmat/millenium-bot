from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')




setup(console=['.\config.py'])

setup(windows=[{
    'script':'vote.py',
    'icon_resources':[(1, 'wow.ico')]
}])

#setup(windows=[{
#    'script':'HttpProxy_Build.py',
#    'icon_resources':[(1, 'wow.ico')]
#}])


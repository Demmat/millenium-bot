import sys
import pygtk
if not sys.platform == 'win32':
    pygtk.require('2.0')
import gtk
import os

print 'initial sysarg',sys.argv[0]
print os.path.dirname(os.getcwd())

from config_gui import Win

if __name__ == '__main__':
    # enable threading
    gtk.threads_init()
    gtk.threads_enter()

    # create the main window
    myapp = Win()

    # start the program loop
    gtk.main()

    # cleanup
    gtk.threads_leave()
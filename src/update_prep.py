#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 13 juin 2012



@author: maxisoft
'''

import subprocess
import os
import sys

if os.name == 'nt':
        import ctypes
        MessageBox = ctypes.windll.user32.MessageBoxW
else:
    def MessageBox(_arg1=None, s='', _arg3=None, _arg4=None, _arg5=None):
        print s

#----------------------------------------------------------------------
def Killprocess(process):
    """"""
    subprocess.Popen("taskkill /IM %s /F" % (process)).wait()

if __name__ == '__main__':
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass
    
    Killprocess('MillenuimService.exe')
    Killprocess('svote.exe')
    
    MessageBox(None, u'Preparation Mise a jour Ok. \nVeuillez Supprimer le contenu du dossier Puis extraire les Nouveaux fichiers', u'Update Prep', 0)
    
    
    
    
    
    pass
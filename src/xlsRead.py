#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 11 juin 2012

@author: maxisoft
'''
import xlrd
import os
import sys


from config import ProxyConfig

pconfig=ProxyConfig()
if os.name == 'nt':
        import ctypes
        MessageBox = ctypes.windll.user32.MessageBoxW
else:
    def MessageBox(_arg1=None,s='',_arg3=None,_arg4=None,_arg5=None):
        print s

if __name__ == '__main__':
    
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass
    finally:
        os.chdir('./Config')
    doc=None
    
    
    try:
        doc = xlrd.open_workbook('acc.xls')
    except Exception as inst:
        MessageBox(None, unicode(inst), u'Import xls - Millenium Bot', 0)
        raise Exception(str(inst))
    sh = doc.sheet_by_index(0)
    
    index = 1
    for rownum in range(sh.nrows-1):
        
        print sh.row_values(rownum+1),index
        pconfig.setLogin(sh.row_values(rownum+1)[0], sh.row_values(rownum+1)[1],index)
        index+=1
    
    try:
        os.remove('acc.xls')
    except Exception as inst:
        MessageBox(None, unicode(inst), u'Import xls - Millenium Bot', 0)
        raise Exception(str(inst))
    
    MessageBox(None, u'Données importée avec succès.', u'Import xls - Millenium Bot', 0)
    
    print 'ok'

        
         
    pass

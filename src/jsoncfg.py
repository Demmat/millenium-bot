#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 20 juin 2012

@author: maxisoft
'''
import json
import os
import sys


#def changedir():
#    #Changement de dir
#    odldir=os.getcwd()
#    try:
#        os.chdir(os.path.dirname(sys.argv[0]))
#    except:
#        pass
#    finally:
#        os.chdir('./config')
#    #------

class jsoncfg(object):
    
    def __init__(self,filename='./config/config.json'):
        self.filename = filename
        pass
    
    def read(self,file=None):
        '''Lit la config Json'''
        if file==None:
            file=self.filename
            
        ret = None
        olddir = os.getcwd()
        
        try:
            os.chdir(os.path.dirname(sys.argv[0]))
        except:
            pass
        
        with open(file) as fichier:
            ret = json.load(fichier)
            
            
        os.chdir(olddir) # retour a l'ancien dir
            
        return ret
        
    def write(self,obj,file=None):
        if file==None:
            file=self.filename
            
        with open(file,'w') as fichier:
            json.dump(obj, fichier,indent=4)



if __name__ == '__main__':
    jsoncon = jsoncfg()
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12',
    'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
    'Accept-Language': 'en-gb,en;q=0.5',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    'Connection': 'keep-alive'
    }
    towrite = {'checkUrl':'http://maxisoft.tk/MVote/status.php','checkStatut':1}
    #jsoncon.write(towrite)
    print jsoncon.read()
    
    
    pass
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
    
    towrite = {'checkUrl':'http://maxisoft.tk/MVote/status.php','checkStatut':1,}
    #jsoncon.write(towrite)
    print jsoncon.read()
    
    
    pass
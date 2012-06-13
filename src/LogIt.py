#!/usr/bin/python27
# -*- coding: UTF-8 -*-
'''
Created on 2 mai 2012

@author: maxisoft
'''
from time import strftime, localtime, strptime, mktime
import os
import sys

class logit:
    '''Permet d'enregistrer dans un fichier '''
    def __init__(self, logfile="log.txt"):
        self.logfile = logfile
    
    
    def log(self, logtxt):
        try:
            os.chdir(os.path.dirname(sys.argv[0]))
        except:
            pass
        with open(self.logfile, 'a') as log:
            log.write(strftime("%a, %d %b %Y %H:%M:%S", localtime()) + " | " + str(logtxt))
            log.write("\n")
    
    
    def writeTime(self):
        try:
            os.chdir(os.path.dirname(sys.argv[0]))
        except:
            pass
        with open(self.logfile, 'w') as log:
            log.write(strftime("%d/%m/%Y %H:%M", localtime()))
            log.write("\n")
            
    def getTime(self):
        try:
            os.chdir(os.path.dirname(sys.argv[0]))
        except:
            pass
        time = strptime('01/01/2000 00:00', "%d/%m/%Y %H:%M")
        try:
            with open(self.logfile, 'r') as log:
                time = strptime(log.read()[:-1], "%d/%m/%Y %H:%M")
        except:
            pass
            
        return time
    
    
    def difTime(self):
        """ Retourne la differance(en seconde) entre le temps du log et le temps actuel """
        
        return int(mktime(localtime()) - mktime(self.getTime()))







if __name__ == '__main__':
    
    from time import sleep
    
    timelog = logit('time.log')
    
    timelog.writeTime()
    sleep(5)
    print timelog.getTime()
    print timelog.difTime()
    
    
    
    

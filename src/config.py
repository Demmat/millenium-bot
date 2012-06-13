#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 7 juin 2012

@author: maxisoft
'''

import sqlite3
from base64 import b64decode, b64encode

import zlib
import socket
import md5
import os
import sys
import random

from Crypto.Cipher import AES

from time import strftime, localtime, strptime, mktime, time

from LogIt import logit as logclass
logit = logclass()

class config(object):
    '''
    Config du bot
    '''


    def __init__(self):
        '''
        Constructor 
        '''
        try:
            os.chdir(os.path.dirname(sys.argv[0]))
        except:
            pass
        finally:
            os.chdir('./config')
        
        self.voteUrl = 'http://millenium-servers.com/newvoter.php'
        
        self.VoteVerifStr = """var m_url = "newvoter.php?voteID=" + id + "&voteVerif="""
        
        self.urltomake = """?voteID=%s&voteVerif=%s&__c=temp&css=%s""" #%s => a remplacer
        
        #db
        if not os.path.exists('config.db'):
            logit.log("Erreur, retelecharger le programme")
            raise Exception("""Erreur, retelecharger le programme""")
        
        self.conn = sqlite3.connect('config.db')
        self.__c = self.conn.cursor()
        
#    def __del__(self):
#        del(self.__c)
#        self.conn.close()
        
    def getLogin(self):
        '''Retourne un dict contenant l'utilisateur et le password.'''
        
        self.__c.execute('SELECT value FROM "main"."cfg" WHERE param="user"')
        user = str(self.__c.fetchone()[0])
        if user == "_":
            logit.log("Vous devez lancer au moins une fois l'utilitaire de configuration.")
            raise Exception("Vous devez lancer au moins une fois l'utilitaire de configuration.")
        
        self.__c.execute('SELECT value FROM "main"."cfg" WHERE param="passw"')
        passw = self.decrypt(self.__c.fetchone()[0])
        
        return {'user':user, 'passw':passw}
        
        
    def setLogin(self, user, passw):
        user = (str(user),)
        passw = (self.crypt(passw),)
        self.__c.execute("""UPDATE "main"."cfg" SET "value"=? WHERE ("param"='user')""", user)
        self.__c.execute("""UPDATE "main"."cfg" SET "value"=? WHERE ("param"='passw')""", passw)
        self.conn.commit()
        
    def getHeader(self):
        self.__c.execute('SELECT value FROM "main"."cfg" WHERE param="User-Agent"')
        return str(self.__c.fetchone()[0])
    
    def getTopName(self, id):
        id = (int(id),)
        self.__c.execute('SELECT Nom FROM "main"."TOP" WHERE VoteId=?', id)
        return str(self.__c.fetchone()[0])
        
    
    #---------------------------------------
    # Time Here
    
    def writeTime(self):
        '''Ecrit le temps actuel dans la db'''
        curtime = (strftime("%d/%m/%Y %H:%M", localtime()),)
        self.__c.execute("""UPDATE "main"."cfg" SET "value"=? WHERE ("param"='lastrun')""", curtime)
        self.conn.commit()
            
    def getTime(self):
        '''retourne un objet temp qui est stock� dans la db'''
        time = strptime('01/01/2000 00:00', "%d/%m/%Y %H:%M")
        
        try:
            self.__c.execute('SELECT value FROM "main"."cfg" WHERE param="lastrun"')
            time = strptime(str(self.__c.fetchone()[0]), "%d/%m/%Y %H:%M")
        except:
            pass
            
        return time
    
    
    def difTime(self):
        """ Retourne la differance(en seconde) entre le temps du log et le temps actuel """
        
        return int(mktime(localtime()) - mktime(self.getTime()))
        
    #--------------------------------------- 
    # Crypto Here  
    
    def __getComputerMD5Name(self):
        """Pour Crypter le password"""
        return str(md5.new(socket.gethostname()).hexdigest())
    
    
    
    
    def crypt(self, string):
        """Algo de keke ..."""
        
        def encipher(S):
            return AES.new(self.__getComputerMD5Name(),AES.MODE_PGP).encrypt(S)
        
        computerName = self.__getComputerMD5Name()
        string = encipher(string)
        return b64encode(zlib.compress(string) + computerName[0:int(computerName[-1], 16)])
    
    def decrypt(self, cstring):
        """Algo de kiki ..."""
        
        def decipher(S, n=3):
            return AES.new(self.__getComputerMD5Name(),AES.MODE_PGP).decrypt(S)
        
        computerName = self.__getComputerMD5Name()
        return decipher(zlib.decompress(b64decode(cstring).replace(computerName[0:int(computerName[-1], 16)], '')))
    
    def useProxy(self):
        try:
            os.chdir(os.path.dirname(sys.argv[0]))
        except:
            pass
        return os.path.exists('./proxy.txt') # TODO mieux
    
        
### -------------------------------------------       

 
class ProxyConfig(config):
    
    def __init__(self):
        config.__init__(self)
        self.__c = self.conn.cursor()
        
        
    def setLogin(self , user, passw, id=None):
        sqlparma = [str(user), self.crypt(passw), ]
        if id != None:
            sqlparma.insert(0, int(id))
            self.__c.execute("""INSERT OR REPLACE INTO "main"."multiacc" (prior, user, passw) VALUES (?, ?, ?);""", sqlparma)
            self.conn.commit()
        else:
            self.__c.execute("""INSERT OR REPLACE INTO "main"."multiacc" (user, passw) VALUES (?, ?);""", sqlparma)
            self.conn.commit()
    
    def writeTime(self, user=None):
        
        config.writeTime(self)
        if user != None:
            #print time()
            self.__c.execute("""UPDATE "main"."multiacc" SET "lastVote"=strftime('%s','now') WHERE ("user"=?);""", (str(user),))
            self.conn.commit()
            
    def getReadyacc(self):
        '''Retourne un tuple de dict de tous les comptes qui on voté il y a plus de 2h'''      
        self.__c.execute(
         """SELECT
                multiacc.user,
                multiacc.passw
            FROM
                multiacc
            WHERE
                strftime('%s', 'now') - multiacc.lastVote > ?
            GROUP BY
                multiacc.user
            ORDER BY
                multiacc.prior ASC ;""",(int(2*60*60+random.random()*60*3),))
            
        return tuple({'user':str(item[0]),'passw':self.decrypt(item[1])} for item in self.__c.fetchall())
    
        
        
        
    
### -------------------------------------------        

if __name__ == '__main__':
    debug = 0
    
    if debug:
        a = ProxyConfig()
#        a = config()
        print a.getTime()
        a.writeTime()
        print a.getTime()
        print a.difTime()
        print a.getTopName(3)
        print a.getReadyacc()
        #a.setLogin('coucou', 'passw')
        #a.writeTime('se')
        
        
    else:
        a = config()
        print """
    
     __      __   _         ____        _   
     \ \    / /  | |       |  _ \      | |  
      \ \  / /__ | |_ ___  | |_) | ___ | |_ 
       \ \/ / _ \| __/ _ \ |  _ < / _ \| __|
        \  / (_) | ||  __/ | |_) | (_) | |_ 
         \/ \___/ \__\___| |____/ \___/ \__|
                                            
                                            
    
    
        """
    
        print '---  Configuration  ---'
        a.setLogin(str(raw_input("\n\nEntrez le nom d'Utilisateur\n")).strip(), str(raw_input("\n\nEntrer le mot de passe\n")).strip())
        raw_input('\n\n Ok. Vous pouvez lancer le bot maintenant')
        
        #print a.getLogin()
    pass

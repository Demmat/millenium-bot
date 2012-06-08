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

class config(object):
    '''
    Config du bot
    '''


    def __init__(self):
        '''
        Constructor 
        '''
        
        os.chdir(os.path.dirname(sys.argv[0]))
        
        self.voteUrl = 'http://millenium-servers.com/newvoter.php'
        
        self.VoteVerifStr = """var m_url = "newvoter.php?voteID=" + id + "&voteVerif="""
        
        self.urltomake = """?voteID=%s&voteVerif=%s&__c=temp&css=%s"""
        
        #db
        self.__conn = sqlite3.connect('config.db')
        self.__c = self.__conn.cursor()
        
    def getLogin(self):
        '''Retourne un dict contenant l'utilisateur et le password.'''
        
        self.__c.execute('SELECT value FROM "main"."cfg" WHERE param="user"')
        user = str(self.__c.fetchone()[0])
        if user == "_":
            raise Exception("Vous devez lancer au moins une fois l'utilitaire de configuration.")
        
        self.__c.execute('SELECT value FROM "main"."cfg" WHERE param="passw"')
        passw = self.__decrypt(self.__c.fetchone()[0])
        
        return {'user':user, 'passw':passw}
        
        
    def setLogin(self, user, passw):
        user = (str(user),)
        passw = (self.__crypt(passw),)
        self.__c.execute("""UPDATE "main"."cfg" SET "value"=? WHERE ("param"='user')""", user)
        self.__c.execute("""UPDATE "main"."cfg" SET "value"=? WHERE ("param"='passw')""", passw)
        self.__conn.commit()
        
    def getHeader(self):
        self.__c.execute('SELECT value FROM "main"."cfg" WHERE param="User-Agent"')
        return str(self.__c.fetchone()[0])
        
        
    def __getComputerMD5Name(self):
        """Pour Crypter le password"""
        return str(md5.new(socket.gethostname()).hexdigest())
    
    def __crypt(self, string):
        """Algo de keke ..."""
        
        def encipher(S, n = 3):
            small = "abcdefghijklmnopqrstuvwxyz"
            big   = small.upper()
            size  = len(big)-1
            finale_str = ''
            for c in S:
                if c.islower():
                    if (small.find(c)+n)>size:
                        c = small[(small.find(c)+n)-(size+1)]
                    else:
                        c = small[small.find(c)+n]
                elif c.isupper():
                    if (big.find(c)+n)>size:
                        c = big[(big.find(c)+n)-(size+1)]
                    else:
                        c = big[big.find(c)+n]
                finale_str += c
            return finale_str
        
        computerName = self.__getComputerMD5Name()
        string = encipher(string)
        return b64encode(zlib.compress(string)+computerName[0:int(computerName[-1],16)])
    
    def __decrypt(self, cstring):
        """Algo de kiki ..."""
        
        def decipher(S, n = 3):
            small = "abcdefghijklmnopqrstuvwxyz"
            big   = small.upper()
            size  = len(big)-1
            finale_str = ''
            for c in S:
                if c.islower():
                    if (small.find(c)-n)<0:
                        c = small[size-small.find(c)-(n-1)]
                    else:
                        c = small[small.find(c)-n]
                elif c.isupper():
                    if (big.find(c)-n)<0:
                        c = big[size-big.find(c)-(n-1)]
                    else:
                        c = big[big.find(c)-n]
                finale_str += c
            return finale_str
        
        computerName = self.__getComputerMD5Name()
        return decipher(zlib.decompress(b64decode(cstring).replace(computerName[0:int(computerName[-1],16)],'')))
        
        
        
        
if __name__ == '__main__':
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

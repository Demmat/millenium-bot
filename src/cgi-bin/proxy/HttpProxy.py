#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-


'''
Created on 4 mai 2012

@author: maxisoft
'''

print 'Content-type: text/html'
print
print '<html><head><title>...'
print '''Proxy</title>
     </head>
     <body>
          <p></p>
     </body>
</html>'''

import cgitb
cgitb.enable()

import re
import time
import urllib2
import cookielib


from MyUrlOpener import urlOpener
from ThreadPool import ThreadPool
from ThreadPool import timeout as tmout





def getMyIp(urlO=None):
    '''Retourne l'adresse IP
    On peut fournir un Opener d'url'''
    if isinstance(urlO, urllib2.OpenerDirector):
        try:
            return urlO.open('http://maxisoft4.tk/ip.php').read(50)
        except:
            try:
                return urlO.open('http://maxisoft3.tk/ip.php').read(50)
            except:
                try:
                    return urlO.open('http://maxisoft.tk/ip.php').read(50)
                except:
                    pass # Return None
    
    return urlOpener.open('http://maxisoft4.tk/ip.php').read(50)


#### -------------------------------------------
class Proxy():
    '''Stocke un Proxy HTTP, c'est a dire son adresse et son port'''
    
    def __init__(self, addresse, port):
        self.url = addresse
        self.port = port      
    
    def __call__(self):
        ''''''
        return { 'host' : str(self.url), 'port' : int(self.port)}
    
    def __str__(self):
        return str(self.url) + ':' + str(self.port)
    
    def makeTheUrlOpener(self):
        '''Crée un objet urllib2 opener avec le Proxy'''
        # On cree un handler pour le Proxy et pour les cookies:
        proxy_support = urllib2.ProxyHandler({"http" : "http://%(host)s:%(port)d" % self()})
        cookiejar = cookielib.CookieJar()
        return urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar), proxy_support)
                    
    #----------------------------------------------------------------------
    def verif(self, verif=False):
        """Tente de se connecter avec le Proxy"""

        
        try:
            urlO = tmout(self.makeTheUrlOpener,timeout_duration=15)
            ip = tmout(getMyIp,(urlO,)) #getMyIp(urlO)
            
            if verif:
                ip.index(str(self.url))
            if not ip:
                raise Exception('Impossible de se connecte en moins de 30 sec')
            
        
        except Exception as inst:
            print '\terreur de Proxy : %s' % (inst)
            #print type(inst) # the exception instance
            #print inst.args # arguments stored in .args
            pass
        else:
            print '- Proxy Ok -'
            return True



#### -------------------------------------------
class ProxyRot():
    '''Gestion de multiples proxys
    on call : retourne un urlOpener du prochain proxy en cours'''
    
    
    #### ------------- Magic Methods -------------
    def __init__(self):
        self.goodproxy = []
        self.indice = 0
        
    def __iter__(self):
        return iter(self.goodproxy)
    
    def __len__(self):
        return len(self.goodproxy)
    
    def __getitem__(self, key):
        return self.goodproxy[key]
    
    
    def __setitem__(self, key, value):
        if isinstance(value, Proxy):
            self.goodproxy[key] = value
            
    def __delitem__(self, key):
        del self.goodproxy[key]
    
    def __call__(self):
        '''Retourne l'urlopener du prochain Proxy sur la liste. '''
        return self.nextGoodProxy().makeTheUrlOpener()
        
    #### --------------------------
    
    def getCurrentProxy(self):
        return self.goodproxy[self.indice]
    def verifAllProxy(self, pfile='Proxy.txt', out=None, threadnbr=15):
        '''Verification de tous les proxys du fichier (pfile).
        Peut enregistrer le Proxy verifier dans un fichier (out)
        Methode a amelioré. '''
        proxys = self.getProxysFromFile(pfile)
        
#        def killthread(thread, timeout=30):
#            """C'est pas beau !"""
#            time.sleep(timeout)
#            if thread.isAlive():
#                thread._Thread__stop()
                
        def verifT(prox):
            if prox.verif():
                self.goodproxy.append(prox)
            
            
        pool = ThreadPool(threadnbr)
        for prox in proxys:
            pool.queueTask(verifT, prox)
            
        timeout = (len(proxys) / threadnbr * 30 + 5) * 1.5
        print 'Temps max : %s' % timeout
        #time.sleep(timeout)
        #print 'arret'
        
        #print self.goodproxy
        
        #TOTO mieux
        count = 0
        while pool.getThreadCount()>0:
            time.sleep(1)
            count+=1
            if count>timeout:
                pool.joinAll(False, False)
            #print pool.getThreadCount()
        
        if out != None:
            with open(out, 'w') as pvfile:
                for Proxy in self.goodproxy:
                    print str(Proxy)
                    pvfile.write(str(Proxy) + '\n')
        
        
                        
                        
                        
    def getProxysFromFile(self, pfile='proxy.txt', force=False):
        '''Retourne un tableau de tous les proxys d'un fichier.'''
        proxytmp = []
        
        with open(pfile) as proxylist:
            proxytmp = proxylist.readlines()
    
    
        proxys = []
    
        for unformated in proxytmp:
            prox = Proxy(str(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', unformated)[0]), int(re.findall('\:\d{1,4}', unformated)[0][1:]))
            proxys.append(prox)
    
        del(proxytmp)
        #for Proxy in proxys:
            #print Proxy
        if force:
            self.goodproxy = proxys
        return proxys
    
    def nextGoodProxy(self):
        '''retourne le prochain Proxy valide de la liste'''
        
        #TODO : yield 
        #for prox in self.__goodproxy:
            
        try:
            while not self.goodproxy[self.indice].verif():
                self.indice += 1
                
            proxy = self.goodproxy[self.indice]
        except:
            raise Exception('Pas asser de proxys.')
        self.indice += 1
#        if self.indice == len(self.__goodproxy):#reset
#            self.indice = 0
        return proxy
        
  
        
if __name__ == '__main__':
    
    
    debug = 0
    
    
    
    if debug:
#        prox = Proxy('121.96.83.151', 80)
#        print prox()
#        prox.verif()
        proxs = ProxyRot()
        proxs.getProxysFromFile('vproxy.txt',force=1)
        #print proxs.goodproxy
        #print proxs.nextGoodProxy()
        print proxs()
    else:
        
    
        print """Verificateur de Proxys ..."""
#    
        import os
        import sys
        import shutil
        import signal
        
        pfile = 'proxy.txt'
        save = 'vproxy.txt'
        try:
			os.chdir(os.path.dirname(sys.argv[0])) 
        except:
            pass
        try:
            os.mkdir('bck')
        except:
            pass
        
        try:
            shutil.copyfile(save, 'bck/vproxy%s' % (time.strftime("%d_%m_%Y-%H%M", time.localtime())))    #pr.verifAllProxy('vproxy.txt')
        except:
            pass
        if len(sys.argv) == 3:
            pfile = sys.argv[1]
            save = sys.argv[2]
            
        proxs = ProxyRot()
        
        def countnombrligne(pfile):
            #pf = open('a')
            with open(pfile, 'r') as pf:
                return len(pf.readlines())
            
            
            
        proxs.verifAllProxy(pfile, out='vproxy.txt', threadnbr=40)
        os.kill(os.getpid(), signal.SIGINT) # TODO pas de kill a la keke
        
    
#        
#    
#    pr = Proxy()
#    pr.verifAllProxy(pfile, save)
#    
##    os.mkdir("bck" )
##    os.chdir("bck")
##    os.mkdir("vproxy" )
#  
#
#    
#    pr.getverifproxys(save)
#    pr.changeIp()
#    pass

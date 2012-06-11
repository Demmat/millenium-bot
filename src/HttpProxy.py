#!/usr/bin/python
# -*- coding: UTF-8 -*-


'''
Created on 4 mai 2012

@author: maxisoft
'''
import re
import time
import urllib2
import cookielib
from Queue import Queue


from MyUrlOpener import urlOpener
from ThreadPool import ThreadPool





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
class proxy():
    '''Stocke un proxy HTTP, c'est a dire son adresse et son port'''
    
    def __init__(self, addresse, port):
        self.url = addresse
        self.port = port      
    
    def __call__(self):
        ''''''
        return { 'host' : str(self.url), 'port' : int(self.port)}
    
    def __str__(self):
        return str(self.url) + ':' + str(self.port)
    
    def makeTheUrlOpener(self):
        '''Crée un objet urllib2 opener avec le proxy'''
        # On cree un handler pour le proxy et pour les cookies:
        proxy_support = urllib2.ProxyHandler({"http" : "http://%(host)s:%(port)d" % self()})
        cookiejar = cookielib.CookieJar()
        return urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar), proxy_support)
                    
    #----------------------------------------------------------------------
    def verif(self, verif=False):
        """tente de se connecter avec le proxy"""

        urlO = self.makeTheUrlOpener()
        try:
            ip = getMyIp(urlO)
            if verif:
                ip.index(str(self.url))
            
        
        except Exception as inst:
            print '\terreur de proxy : %s' % (inst)
            #print type(inst) # the exception instance
            #print inst.args # arguments stored in .args
            pass
        else:
            print '- Proxy Ok -'
            return True



#### -------------------------------------------
class proxyroller():
    '''Gestion de multiples proxys'''
    def __init__(self):
        self.goodproxy = []
        self.indice = int(0)
        
        
        
    def verifAllProxy(self, pfile='proxy.txt', out=None, threadnbr=15):
        '''Verification de tous les proxys du fichier (pfile).
        Peut enregistrer le proxy verifier dans un fichier (out)
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
        time.sleep(timeout)
        #print 'arret'
        pool.joinAll(False, False)
        #print self.goodproxy
        
        if out != None:
            with open(out, 'w') as pvfile:
                for proxy in self.goodproxy:
                    print str(proxy)
                    pvfile.write(str(proxy) + '\n')
        
        
                        
                        
                        
    def getProxysFromFile(self, pfile='proxy.txt', force=False):
        '''Retourne un tableau de tous les proxys d'un fichier.'''
        proxytmp = []
        
        with open(pfile) as proxylist:
            proxytmp = proxylist.readlines()
    
    
        proxys = []
    
        for unformated in proxytmp:
            prox = proxy(str(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', unformated)[0]), int(re.findall('\:\d{1,4}', unformated)[0][1:]))
            proxys.append(prox)
    
        del(proxytmp)
        #for proxy in proxys:
            #print proxy
        if force:
            self.goodproxy = proxys
        return proxys
    
    def nextproxy(self):
        '''retourne le prochain proxy de la liste'''
        try:
            while not self.__goodproxy[self.indice].verif():
                self.indice += 1
                
            proxy = self.__goodproxy[self.indice]
        except:
            raise Exception('Pas asser de proxys.')
        self.indice += 1
#        if self.indice == len(self.__goodproxy):#reset
#            self.indice = 0
        return proxy
        
  
        
if __name__ == '__main__':
    
    
    debug = 0
    
    
    
    if debug:
        prox = proxy('121.96.83.151', 80)
        print prox()
        prox.verif()
        proxs = proxyroller()
        for prox in proxs.getProxysFromFile():
            print prox
        proxs.verifAllProxy(out='vproxy.txt', threadnbr=50)
        for prox in proxs.goodproxy:
            print prox
        while 1:
            print proxs.nextproxy()
    else:
        
    
        print """Verificateur de Proxys ..."""
#    
        import os
        import sys
        import shutil
        import signal
        
        pfile = 'proxy.txt'
        save = 'vproxy.txt'
        os.chdir(os.path.dirname(sys.argv[0])) 
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
            
        proxs = proxyroller()
        proxs.verifAllProxy(pfile, out='vproxy.txt', threadnbr=250)
        os.kill(os.getpid(), signal.SIGINT) # TODO pas de kill a la keke
        
    
#        
#    
#    pr = proxy()
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

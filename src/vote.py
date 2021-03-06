#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 7 juin 2012

@author: maxisoft
'''




import config as cfg

import re

import LogIt

# nav on Web import

import urllib
import urllib2

import args
import MyUrlOpener

from time import sleep
from random import random





#Globals

urlOpener = MyUrlOpener.urlOpener

config = cfg.config()

pageVote = "" #Global contenant la page de vote

request_headers = { 'User-Agent': config.getHeader() }

log = LogIt.logit()




def dlPageVote():
    """Telecharge la page de vote en memoire"""
    global pageVote
    request = urllib2.Request('http://millenium-servers.com/newvoter.php', None, request_headers)
    url = urlOpener.open(request)
    pageVote = url.read(500000) # on lit tout
    

def getVoteVerif():
    """Recupere le 'voteVerif' constituer d'hex."""
    index = pageVote.find("""var m_url = "newvoter.php?voteID=" + id + "&voteVerif=""") + \
            len("""var m_url = "newvoter.php?voteID=" + id + "&voteVerif=""")
    return pageVote[index:pageVote.find('&', index, index + 50)]


def decoupe():
    """Retourne les sous parties importantes de la page."""
    
    return pageVote.split('style type="text/css"')[2:]  #decoupe la page La partie 
                                                    #0 correspond aux heads
                                                    #La partie 1 correspond a gowndowa
                                                    #La partie 2 et 3 correspondent a RPGparadise
    
def getHex(souspage):
    """recherche le doublon hex"""
    pat = re.compile(r'\s+') #supprime tous les chars echapés
    hexs = [pat.sub('', x).replace('{display:inline;}', '')[1:] 
         for x in re.findall(r"\.+.+\n+{display : inline;}", souspage)] # outch !
    for hex in hexs:
        if souspage.count(hex) > 1: # => yen a au moin deux ...
            return hex
        
    #si pas trouve
    raise Exception('Erreur source incorrecte')
    
    
def getcss(souspage, hex):
    """Retourne le css (necessite le hex)"""
    abc = re.findall(r""".{27}class="%s\"""" % (hex), souspage)[0] #il y en a que un normalement
    return abc.split(',')[2].strip()
    
    
def login(user, passw):
    """Connexion au site http://millenium-servers.com .
    Retourne True si connexion ok."""
    values = {'connexion_username': str(user), 'connexion_password': passw, 'connexion_active':'yes'} 
    data = urllib.urlencode(values)
    request = urllib2.Request("http://millenium-servers.com/index.php", data, request_headers)
    url = urlOpener.open(request)  #  cookiejar reçoit automatiquement les cookies
    return url.read(5000000).find(str(user)) != -1
    
    #print page




    
def main(user=None, passw=None):
    '''Do all ...
    Retourne 1 si vote ok'''
    
    #on cherche les identifiants
    if not user or not passw:   #id pas en param
        __login = args.getargs() #en argument ?
        
        if not  __login:    #id pas en arguments
            __login = config.getLogin() #Id dans la DB
        
        user = str(__login['user'])
        
    else: # autement id en param
        __login = {'user':user, 'passw':passw}
    
    #on se log et on obtient un cookie :)
    if not login(user, __login['passw']):
        log.log('Erreur lors de la connexion, identifiant mauvais ? | %s' %(user))
        raise Exception('Erreur lors de la connexion, identifiant mauvais ?')
    
    del (__login)
    #print getVoteVerif()
    
    VoteId = 3  #voir la fonction javascript
        
    sleep(random()*7)#Wait max 7 sec (pour simulé un vote cpatcha)
    
    dlPageVote()
    try:
        souspage = decoupe()[0]
    except:
        log.log('Erreur source incorrecte (deja vote ?)| %s' %(user))
        raise Exception('Erreur source incorrecte (deja vote ?)')
    
    css = getcss(souspage, getHex(souspage))
    
    request = urllib2.Request('http://millenium-servers.com/newvoter.php' + \
                  str("""?voteID=%s&voteVerif=%s&c=temp&css=%s""" % (VoteId, getVoteVerif(), css)), None, request_headers)
    url = urlOpener.open(request)
    
    if str(url.read(500000)).find('OK_VOTE') != -1: # sucess
        success = 'Vote reussi avec %s sur %s' % (user, config.getTopName(VoteId - 1))
        print success
        log.log(success)
        config.writeTime()
        return 1
        
    
    







if __name__ == '__main__':
    try:
        main()
    except Exception as inst:
            print inst # __str__ allows args to printed directly
            #proxy.changeIp()
    finally:
        raw_input('\n\n>>> Tapez entre pour continue')







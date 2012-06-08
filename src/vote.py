#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 7 juin 2012

@author: maxisoft
'''




import config as cfg

import re

# nav on Web import
import cookielib
import urllib
import urllib2


#Globals

config = cfg.config()

pageVote = "" #Global contenant la page de vote

request_headers = { 'User-Agent': config.getHeader() }




# On active le support des cookies pour urllib2
cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))




def dlPageVote():
    """Telecharge la page de vote en memoire"""
    global pageVote
    request = urllib2.Request(config.voteUrl, None, request_headers)
    url = urlOpener.open(request)
    pageVote = url.read(500000) # on lit tout
    

def getVoteVerif():
    """Recupere le 'voteVerif' constituer d'hex."""
    index = pageVote.find(config.VoteVerifStr) + len(config.VoteVerifStr)
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


    
def main():
    __login = config.getLogin()
    if not login(__login['user'], __login['passw']):
        raise Exception('Erreur lors de la connexion, identifiant mauvais ?')
    
    del (__login)
    #print getVoteVerif()
    VoteId = 3
    while VoteId < 5:
        dlPageVote()
        try:
            souspage = decoupe()[0]
        except:
            raise Exception('Erreur source incorrecte (deja vote ?)')
        #print souspage
        hex = getHex(souspage)
        #print hex
        css = getcss(souspage, hex)
        
        #print config.urltomake % (VoteId, getVoteVerif(), css)
        request = urllib2.Request(config.voteUrl + 
                                   str(config.urltomake % (VoteId, getVoteVerif(), css)), None, request_headers)
        url = urlOpener.open(request)
        VoteId += 1
        print url.read(500000) # on lit tout







if __name__ == '__main__':
    main()







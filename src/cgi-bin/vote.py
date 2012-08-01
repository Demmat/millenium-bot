#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 4 juin 2012

@author: maxisoft
'''

########################################

USER = '___________________________'
PASSW = '___________________________'


ForceLogin = 0 	#Mettre a 1 si erreur 'Identifiant mauvais'
				#Attention Si vos logins sont pas bon ça risque de faire planter le script !

#######################################


import re

# nav on Web import
import cookielib
import urllib
import urllib2

import cgitb
cgitb.enable()


#Globals


pageVote = "" #Global contenant la page de vote

request_headers = { 'User-Agent': 'Mozilla/5.0' }




# On active le support des cookies pour urllib2
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))




def dlPageVote():
    """Telecharge la page de vote en memoire"""
    global pageVote
    request = urllib2.Request('http://millenium-servers.com/newvoter.php', None, request_headers)
    url = urlOpener.open(request)
    pageVote = url.read(500000) # on lit tout
    

def getVoteVerif():
    """Recupere le 'voteVerif' constituer d'hex."""
    index = pageVote.find("""var m_url = "newvoter.php?voteID=" + id + "&voteVerif=""") + len("""var m_url = "newvoter.php?voteID=" + id + "&voteVerif=""")
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
    return url.read(5000000).find(str(user)) != -1 or ForceLogin
    
    #print page


    
def main(user=USER,passw=PASSW):
    if not login(user, passw):
        raise Exception('Erreur lors de la connexion, identifiant mauvais ?')
    
    #print getVoteVerif()
    VoteId = 3
    
    dlPageVote()
    #print pageVote
    try:
        souspage = decoupe()[0]
    except:
        raise Exception('Erreur source incorrecte (deja vote ?)')
    #print souspage
    hex = getHex(souspage)
    #print hex
    css = getcss(souspage, hex)
    
    request = urllib2.Request('http://millenium-servers.com/newvoter.php' + 
                               str("""?voteID=%s&voteVerif=%s&c=temp&css=%s""" % (VoteId, getVoteVerif(), css)), None, request_headers)
    url = urlOpener.open(request)
    print url.read(500000) # on lit tout







if __name__ == '__main__':
    print 'Content-type: text/html'
    print
    print '<html><head><title>...'
    print '''Vote</title>
         </head>
         <body>
              <p>Vote</p>
         </body>
    </html>'''
    try:
        main()
        print 'ok'
    except Exception,strerror:
            print strerror 
            #proxy.changeIp()







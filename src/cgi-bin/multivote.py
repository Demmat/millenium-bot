#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 15 juin 2012

@author: maxisoft
'''


import vote



accs = [
      
      
#Completer/Ajouter Les lignes suivante 
#qui sont au format ('Nomducompte','Motdepasse'), :

#######################################

('toto', 'passw1'),
('acc2', 'passw2'),
('acc3', 'passw3'),
#Vous pouvez en ajouter ...

#######################################

]

#######################################
ForceLogin = 0  #Mettre a 1 si erreur 'Identifiant mauvais'
                #Attention Si vos logins sont pas bon ca risque de faire planter le script 
#######################################





def main():
    
    vote.ForceLogin=ForceLogin
    
    for acc in accs:
        
        print '''<p>--- Vote avec %s ---<br />
                    statut :''' % acc[0]
                    
                    
        try:
            vote.main(acc[0], acc[1])
        except Exception, strerror:
            print strerror
        
        #finally:
            
        print '''<br />
         ---------------------
         </p>'''
        vote.urlOpener = vote.urllib2.build_opener(\
                       vote.urllib2.HTTPCookieProcessor(vote.cookielib.CookieJar()))


if __name__ == '__main__':
    print 'Content-type: text/html'
    print
    print '<html><head><title>'
    print '''Multi-Vote</title>
        </head>
        <body>
             <p>Vote</p>
        </body>
    </html>'''
    main()
    
    
    
    





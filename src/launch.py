'''
Created on 8 juin 2012

@author: maxisoft
'''
import vote
from time import sleep

if __name__ == '__main__':
    while 1:
        try:
            vote.main()
        except Exception as inst:
            if str(inst)=="Vous devez lancer au moins une fois l'utilitaire de configuration.":
                raise Exception("Vous devez lancer au moins une fois l'utilitaire de configuration.")
            if str(inst)=='Erreur lors de la connexion, identifiant mauvais ?':
                raise Exception('Erreur lors de la connexion, identifiant mauvais ?')
            pass
        sleep(2*60*60)
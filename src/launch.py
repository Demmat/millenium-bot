'''
Created on 8 juin 2012

@author: maxisoft
'''
import svote
from time import sleep
from random import random

if __name__ == '__main__':
    while 1:
        try:
            svote.main()
        except Exception as inst:
            if str(inst)=="Vous devez lancer au moins une fois l'utilitaire de configuration.":
                raise Exception("Vous devez lancer au moins une fois l'utilitaire de configuration.")
            elif str(inst)=='Erreur lors de la connexion, identifiant mauvais ?':
                raise Exception('Erreur lors de la connexion, identifiant mauvais ?')
            else: 
                raise Exception(str(inst))
            pass
        sleep(60*60+random()*5*60) #Wait 1h + rand
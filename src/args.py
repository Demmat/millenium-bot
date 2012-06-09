'''
Created on 9 juin 2012

@author: maxisoft
'''

import sys
import getopt

def getargs(argv=sys.argv[1:]):
    '''Analyse les arguments pour chercher le login et le password
    Retourne None si pas de login ni de password'''
    user = "_"
    passw ="_"
    try:
        opts, args = getopt.getopt(argv, "hp:u:",["help",])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-u':
            user = arg
        elif opt == '-p':
            passw = arg
            
    if (user,passw) != ('_','_') :
        return {'user':user,'passw':passw}
            
    
def usage():
    print """Entrez simplement -u NOM_UTILISATEUR -p MOTDEPASSE"""
    
if __name__ == '__main__':
    getargs(sys.argv[1:])
    pass
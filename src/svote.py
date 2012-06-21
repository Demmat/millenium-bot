'''
Created on 9 juin 2012

Pour Service sous Windows

@author: maxisoft
'''
import os
import sys

import proxyVote
import vote
import jsoncfg

import config as cfg

config = cfg.ProxyConfig()
jsonparam = jsoncfg.jsoncfg().read()

def main():
    if jsonparam['checkStatut']:
        ok = 0
        try:
            ok = int(vote.urlOpener.open(jsonparam['checkUrl']+\
                                    '?ver=%s'%(config.getVersionNbr())).read(50))
            if not ok:
                vote.log.log('Erreur, le bot ne semble pas a jour.')
                sys.exit(0)
        except:
            pass
    global config
    
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass
    if not config.useProxy():
        __login = config.getReadyacc()
        
        if __login and config.getLogin() == __login[0]: # Login != None et c'est le premier compte:
            __login = __login[0]
            
            if vote.main(__login['user'], __login['passw']) == 1: #vote success
                print 'vote success'
                config.writeTime(__login['user'])
            
        del(config)
    else:
        print 'proxy mode'
        del(config)
        proxyVote.main()
    


if __name__ == '__main__':
    main()

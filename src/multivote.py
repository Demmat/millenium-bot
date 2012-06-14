'''
Created on 14 juin 2012

@author: maxisoft
'''

import vote

import config as cfg

from MyUrlOpener import updateUrlOp
from ThreadPool import timeout

config = cfg.ProxyConfig()


def oneVote(user,passw):
    '''Recontruit un urlOpener et Vote'''
    updateUrlOp()
    config = cfg.ProxyConfig()
    
    vote.config = config #reafectation pour thread
    try:
        vote.main(user, passw)
    except:
        pass
    else:
        config.writeTime(user=user)
    del (config)
        

def voteall():
    
    global config
    accs = config.getReadyacc()
    del (config)
    print len(accs)
    
    for accinfo in accs:
        print accinfo['user']
        timeout(oneVote, kwargs=accinfo, timeout_duration=100)
#        if res == 1:
#            time_out = 0
##        else:
##            pass
        
        
        #MyUrlOpener.updateUrlOp(proxys())
        #updateVoteUrlO(proxys())


if __name__ == '__main__':
    voteall()
    pass
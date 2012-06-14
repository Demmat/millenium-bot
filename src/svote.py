'''
Created on 9 juin 2012

Pour Service sous Windows

@author: maxisoft
'''
import os
import sys

import proxyVote
import multivote

import config as cfg

config = cfg.config()



if __name__ == '__main__':
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass
    if not config.useProxy():
        del(config)
        multivote.voteall()
    else:
        print 'proxy mode'
        del(config)
        proxyVote.main()

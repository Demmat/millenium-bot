'''
Created on 9 juin 2012

Pour Service sous Windows

@author: maxisoft
'''
import os
import sys
from random import random

import vote
import config as cfg

config = cfg.config()


if __name__ == '__main__':
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass
    if not config.useProxy():
        try:
            print config.difTime()
            if config.difTime() < 2 * 60 * 60 + random() * 5 * 60:
                sys.exit()
            else:
                del(config)
                vote.main()
                
        except Exception as inst:
            print inst #
            pass
    else:
        del(config)
        import proxyVote
        proxyVote.main()

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
        except:
            pass
        sleep(2*60*60)
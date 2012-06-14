#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 10 juin 2012

@author: maxisoft
'''

import cookielib
import urllib2


cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

def updateUrlOp(urlO=None):
    '''Change la ref de la global urlOpener.'''
    import vote
    global urlOpener
    
    if isinstance(urlO, urllib2.OpenerDirector):
        urlOpener = urlO
    else:
        urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    
    try:
        vote.urlOpener = urlOpener
    except:
        pass

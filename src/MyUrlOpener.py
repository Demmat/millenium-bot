'''
Created on 10 juin 2012

@author: maxisoft
'''

import cookielib
import urllib2

cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

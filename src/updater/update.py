#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 13 juin 2012



@author: maxisoft
'''






import subprocess
import os
import sys
import zipfile
import urllib2
import shutil
import urlparse
import os

import __importall #voir __importall !

UpdateUrl = 'https://github.com/downloads/maxisoft/millenium-bot/update.zip'

processName = ('MillenuimService.exe', 'svote.exe', 'vote.exe',
             'proxyVote.exe', 'launch.exe', 'xlsRead.exe', 'HttpProxy.exe',
             'ServiceInstaller.exe', 'update_prep.exe')


if os.name == 'nt':
        import ctypes
        MessageBox = ctypes.windll.user32.MessageBoxW
else:
    def MessageBox(_arg1=None, s='', _arg3=None, _arg4=None, _arg5=None):
        print s

#----------------------------------------------------------------------

def readall(file):
    '''Lit le contenu du fichier et retourne le string'''
    with open(file) as py:
        return "".join(py.readlines())

def download(url, fileName=None):
    def getFileName(url,openUrl):
        if 'Content-Disposition' in openUrl.info():
            # If the response has Content-Disposition, try to get filename from it
            cd = dict(map(
                lambda x: x.strip().split('=') if '=' in x else (x.strip(),''),
                openUrl.info()['Content-Disposition'].split(';')))
            if 'filename' in cd:
                filename = cd['filename'].strip("\"'")
                if filename: return filename
        # if no filename was found above, parse it out of the final URL.
        return os.path.basename(urlparse.urlsplit(openUrl.url)[2])

    r = urllib2.urlopen(urllib2.Request(url))
    try:
        fileName = fileName or getFileName(url,r)
        with open(fileName, 'wb') as f:
            shutil.copyfileobj(r,f)
    finally:
        r.close()
#----------------------------------------------------------------------
def Killprocess(process):
    """"""
    startupinfo = None
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    try:
        subprocess.Popen("taskkill /IM %s /F" % (process), startupinfo=startupinfo).wait()
    except:
        pass

def RunCMD(cmd):
    startupinfo = None
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    try:
        subprocess.Popen(cmd, startupinfo=startupinfo).wait()
    except:
        pass



if __name__ == '__main__':
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass
    
    download(UpdateUrl,'update.zip')
    
    for proc in processName:
        Killprocess(proc)
        
    
    updatef = zipfile.ZipFile('./update.zip')
    
    updatef.extractall()
    
    if os.path.exists('./trigger.py'):
        exec(readall('./trigger.py'))
        os.remove('./trigger.py')
    
    
    MessageBox(None, u'Mise a jour Ok.', u'Update', 0)
    updatef.close()
    os.remove('./update.zip')
    

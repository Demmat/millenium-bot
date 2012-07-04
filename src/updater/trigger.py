import os
import sys
import zipfile
import sqlite3
from time import sleep
version = 3005
currentVersion = 1000 # version 1 par def


try:
	from update import RunCMD,MessageBox,download
except:
	pass

### ----------------- Se place dans le dossier config
try:
	os.chdir(os.path.dirname(sys.argv[0]))
except:
	pass
finally:
	os.chdir('./config')
	
	
	

### ----------------- Regarde si nouvelle install.
if not os.path.exists('config.db'):
	print 'extract'
	updatef = zipfile.ZipFile('./config_original.zip')

	updatef.extractall()
	
	


### ----------------- DB Update
with sqlite3.connect('config.db',isolation_level=None) as conn:
	c_Version = currentVersion
	c=conn.cursor()
		
	
		#try to get current version & update
	try:
		c.execute('SELECT value FROM "main"."cfg" WHERE param="Version"')
		
		currentVersion = int(c.fetchone()[0])
		print currentVersion
		conn.execute('REPLACE INTO "main"."cfg" VALUES ("Version", ?)',(str(version),))
		conn.commit()
		c.close()
	except Exception,stre:
		print stre
		pass



### Update password crypt
if currentVersion<2050:
	MessageBox(None, u'Vous devez reconfigurer le Bot !', u'update', 0)
	updatef = zipfile.ZipFile('./config_original.zip')
	updatef.extractall()
	
### Get config Gui
try:
	os.chdir(os.path.dirname(sys.argv[0]))
except:
	pass
if currentVersion<3001 or not os.path.exists('config.exe'):
	download('https://github.com/downloads/maxisoft/millenium-bot/config.exe','config.exe')



### ----------------- restart le service
try:
	RunCMD('sc start "MillenuimBot"') 
except:
	pass


### Retour au repertoir de depart 
try:
	os.chdir(os.path.dirname(sys.argv[0]))
except:
	pass

#print currentVersion

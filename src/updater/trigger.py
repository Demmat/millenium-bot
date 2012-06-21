import os
import sys
import zipfile
import sqlite3

version = 2100
currentVersion = 1000 # version 1 par def

try:
	from update import RunCMD,MessageBox
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
	updatef = zipfile.ZipFile('./config_original.zip')

	updatef.extractall()
	
	
	
	
### ----------------- DB Update
conn = sqlite3.connect('config.db')
c=conn.cursor()

	#Delete old and useless
c.execute("""DELETE FROM "main"."cfg" WHERE ("param"='user')""")
c.execute("""DELETE FROM "main"."cfg" WHERE ("param"='passw')""")
conn.commit()
	
	#try to get current version
try:
	c.execute('SELECT value FROM "main"."cfg" WHERE param="Version" LIMIT 1')
	currentVersion = c.fetchone()[0]
except:
	pass
	
	
	#Update vers
c.execute("""INSERT OR REPLACE INTO "main"."cfg" ("param", "value") VALUES ('Version', %s);"""%(version))
conn.commit()

	
	#Delete cursor & Db
c.close()
del(c);del(conn)






### Update password crypt
if currentVersion<2050:
	MessageBox(None, u'Vous devez reconfigurer le Bot !', u'update', 0)
	updatef = zipfile.ZipFile('./config_original.zip')
	updatef.extractall()
	




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

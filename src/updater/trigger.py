import os
import sys
import zipfile
try:
	from update import RunCMD
except:
	pass

##### Se place dans le dossier config
try:
	os.chdir(os.path.dirname(sys.argv[0]))
except:
	pass
finally:
	os.chdir('./config')

##### Regarde si nouvelle install.
if not os.path.exists('config.db'):
	updatef = zipfile.ZipFile('./config_original.zip')

	updatef.extractall()
	

### restart le service
try:
	RunCMD('sc start "MillenuimBot"') 
except:
	pass


### Retour au repertoir de depart 
try:
	os.chdir(os.path.dirname(sys.argv[0]))
except:
	pass

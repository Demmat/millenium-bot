Dans ce Dossier se trouve un script python simplifier pour voter sur millenuim 
( ie pas d'utilisation de sqlite ni de class config et autre fonctionnalité )

Pour l'installer sur un server web possedant cgi-python (on peut aussi le mettre sur Google app engine), 

	Il faut tout d'abord configurer le script pour cela :
	
		ouvrez 'vote.py' du dossier 'cgi-bin' (avec notepad par ex sous windows)
		Completez USER (ligne 12) en remplacant '___________________________' par 'LeNomdeVotreCompte'
		Completez PASSW (ligne 13) en remplacant '___________________________' par 'LeMotdePasse'
		
	La configuration est alors terminé.

	Puis il suffit de copier 'vote.py' dans le dossier 'cgi-bin' de votre site (dossier www, public_html, ect...) par FTP par ex.
	Ensuite, un chmod 755 et c'est Tout bon.

Vous pouvez alors appeler le script en tapant http://votresite.cc/cgi-bin/vote.py   .


Bonus :

Sur la pluspars des sites, on peut effectuer des crons .

Il suffit donc de créé un cron se lançant toutes les 2h avec la cmd suivante :
wget -O - http://votresite.cc/cgi-bin/vote.py

Cela permet de lancer le script toutes les 2h automatiquement.

